#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[4]:


import random
class Card:
    SUIT_SYMBOLS = {
        'Hearts': '♥',   # ♥
        'Diamonds': '♦', # ♦
        'Clubs': '♣',    # ♣
        'Spades': '♠'    # ♠
    }
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        suit_symbol = self.SUIT_SYMBOLS[self.suit]
        return f"{self.rank} {suit_symbol}"
    
    
    
class Deck:
    def __init__(self): 
        """
        Represents a standard deck of 52 cards.
        """
        suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self.cards)

    def deal(self, num_cards):
        """
        Deals a specified number of cards from the top of the deck.
        :param num_cards: Number of cards to deal.
        :return: A list of Card objects.
        """
        if num_cards > len(self.cards):
            num_cards = len(self.cards)  # Adjust to deal only the remaining cards.
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]  # Remove dealt cards from the deck.
        return dealt_cards
    
    
    
    
class Player:
    def __init__(self, name):
        """
        Represents a player in the game.
        :param name: The name of the player.
        """
        self.name = name
        self.hand = []  # List of Card objects in the player's hand
        self.books = []  # List of completed books (ranks with 4 cards)
        self.previous_queries = set()  # ISADORA ADDED THIS: Set of ranks the player has already asked for

    def add_cards(self, cards):
        """
        Adds cards to the player's hand.
        :param cards: A list of Card objects to add.
        """
        self.hand.extend(cards)

    def sort_hand(self):
        """
        Sorts the player's hand using insertion sort.
        """
      
        def card_rank_value(card):
            # Custom sorting by rank order (Ace to King)
            rank_order = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
            return rank_order.index(card.rank)

        for i in range(1, len(self.hand)):
            key_card = self.hand[i]
            j = i - 1
            while j >= 0 and card_rank_value(self.hand[j]) > card_rank_value(key_card):
                self.hand[j + 1] = self.hand[j]
                j -= 1
            self.hand[j + 1] = key_card

    def search_rank(self, rank):
        """
        Searches for a specific rank in the player's sorted hand using binary search.
        :param rank: The rank to search for.
        :return: Index of the card if found; -1 otherwise.
        """
        self.sort_hand()  # Make sure the hand is sorted before searching
        left, right = 0, len(self.hand) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.hand[mid].rank == rank:
                return mid
            elif self.hand[mid].rank < rank:
                left = mid + 1
            else:
                right = mid - 1
        return -1  # Rank not found

    def make_books(self):
        """
        Identifies and removes books (sets of 4 cards of the same rank) from the player's hand.
        Returns the ranks of completed books.
        """
        rank_counts = {}
        for card in self.hand:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

        completed_books = []
        for rank, count in rank_counts.items():
            if count == 4:
                completed_books.append(rank)
                self.books.append(rank)
                self.hand = [card for card in self.hand if card.rank != rank]

        return completed_books

    def give_all_of_rank(self, rank):
        """
        Removes all cards of the specified rank from the player's hand.
        :param rank: The rank of cards to be removed (e.g., '5').
        :return: A list of Card objects of the specified rank.
        """
        matching_cards = [card for card in self.hand if card.rank == rank]
        self.hand = [card for card in self.hand if card.rank != rank]
        return matching_cards
    
    

class GoFishGame:
    def __init__(self):
        """
        Manages the overall game mechanics, including players and the deck.
        """
        self.deck = Deck()
        self.players = []

    def add_player(self, player):
        """
        Adds a player to the game.
        :param player: A Player object.
        """
        self.players.append(player)

    def setup_game(self):
        """
        Shuffles the deck and deals initial hands to all players.
        """
        self.deck.shuffle()
        for player in self.players:
            player.add_cards(self.deck.deal(7))

    def player_ask_for_rank(self, player, opponent, rank_to_ask, is_cpu=False):
        """
        Handles a player's turn to ask another player for a specific rank.
        :param player: The player asking for a rank.
        :param opponent: The player being asked.
        :param rank_to_ask: The rank to ask for.
        :param is_cpu: Boolean indicating whether the player is a CPU.
        """
        if not any(card.rank == rank_to_ask for card in player.hand):
            print(f"{player.name} can't ask for a rank they don't have.")
            return

        print(f"{player.name} asks {opponent.name}: Do you have any {rank_to_ask}s?")
        matching_cards = opponent.give_all_of_rank(rank_to_ask)

        if matching_cards:
            print(f"{opponent.name} gives cards with rank {rank_to_ask}:")
            player.add_cards(matching_cards)
            for card in matching_cards:
                print(card)

            # Check for books after receiving cards from the opponent
            completed_books = player.make_books()
            if completed_books:
                print(f"{player.name} completes a book of {', '.join(completed_books)}!")
        else:
            print(f"{opponent.name} says: Go Fish!")
            if self.deck.cards:
                new_card = self.deck.deal(1)[0]
                player.add_cards([new_card])
                if is_cpu:
                    print(f"{player.name} draws a card.")
                else:
                    print(f"{player.name} draws a card: {new_card}")

                # Check for books after drawing a card from the deck
                completed_books = player.make_books()
                if completed_books:
                    print(f"{player.name} completes a book of {', '.join(completed_books)}!")
            else:
                print("No cards left in the deck!")

    def play_turn(self, player, opponent):
        """
        Executes a single turn for a player.
        """
        if not player.hand:
            print(f"{player.name} has no cards to play and skips their turn.")
            return

        # Ensure `previous_queries` is initialized
        if not hasattr(player, "previous_queries"):
            player.previous_queries = set()

        # Get rank counts in the player's hand
        rank_counts = {card.rank: sum(1 for c in player.hand if c.rank == card.rank) for card in player.hand}

        # Filter out ranks already asked
        available_ranks = [rank for rank in rank_counts if rank not in player.previous_queries]

        # Reset `previous_queries` if all ranks have been asked
        if not available_ranks:
            print(f"{player.name} has asked for all possible ranks. Resetting queries.")
            player.previous_queries.clear()
            available_ranks = list(rank_counts.keys())

        # Skip turn if no ranks are available after reset
        if not available_ranks:
            print(f"{player.name} has no valid ranks to ask. Skipping turn.")
            return

        # Choose the most frequent rank or the first available rank
        rank_to_ask = max(rank_counts, key=lambda rank: rank_counts[rank])

        print(f"{player.name} decides to ask for {rank_to_ask}s.")
        player.previous_queries.add(rank_to_ask)

        # Execute the rank query
        self.player_ask_for_rank(player, opponent, rank_to_ask)

        # If the player's hand is empty after the turn, they skip future turns
        if not player.hand:
            print(f"{player.name}'s hand is now empty.")

    def is_game_over(self):
        """
        Determines if the game is over.
        """
        if self.deck.cards:
            return False

        all_hands_empty = all(len(player.hand) == 0 for player in self.players)
        if all_hands_empty:
            return True

        for player in self.players:
            for opponent in self.players:
                if player != opponent:
                    if any(card.rank in [op_card.rank for op_card in opponent.hand] for card in player.hand):
                        return False

        return True

    
    def show_player_books(self):
        """
        Displays the books collected by all players.
        """
        print("\nFinal Books:")
        for player in self.players:
            print(f"{player.name}'s Books: {player.books}")

    def determine_winner(self):
        """
        Determines the winner of the game based on the number of books collected.
        """
        max_books = max(len(player.books) for player in self.players)
        winners = [player for player in self.players if len(player.books) == max_books]

        if len(winners) > 1:
            print("\nIt's a tie!")
        else:
            print(f"\nThe winner is {winners[0].name} with {max_books} books!")
            
            
    


# In[8]:


def main():
    print("Welcome to the Go Fish Game!")  # Welcome message

    human_name = None
    while not human_name:
        try:
            # Ask for the human player's name
            human_name_input = input("Please enter your name: ").strip()
            if not human_name_input or not human_name_input.isalpha():
                raise ValueError("Name must contain only alphabetic characters and cannot be empty.")
            human_name = human_name_input  # Assign only if the input is valid
        except ValueError as ve:
            print(f"Input error: {ve}")

    # Create human and CPU players
    human = Player(human_name)  
    cpu = Player("CPU")  

    # Create the game instance
    game = GoFishGame()
    game.add_player(human)
    game.add_player(cpu)

    try:
        # Setup the game
        game.setup_game()

        # Display initial hands
        print(f"\nWelcome, {human.name}! You will be playing against {cpu.name}.")
        print(f"{human.name}'s Initial Hand: {', '.join(str(card) for card in human.hand)}")
        print(f"{cpu.name}'s hand is hidden.")

        # Game loop
        turn = 0
        valid_ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        while not game.is_game_over():
            try:
                if turn % 2 == 0:  # Human's turn
                    print(f"\n{human.name}'s Turn:")
                    print(f"Your Hand: {', '.join(str(card) for card in human.hand)}")

                    # Get a valid rank from the human
                    while True:
                        rank_to_ask = input("Enter the rank you want to ask for (e.g., '5', 'Ace', 'Queen'): ").strip()
                        if rank_to_ask in valid_ranks and any(card.rank == rank_to_ask for card in human.hand):
                            break
                        print("Invalid rank! Please choose a valid rank from your hand.")
                    
                    game.player_ask_for_rank(human, cpu, rank_to_ask)
                else:  # CPU's turn
                    print(f"\n{cpu.name}'s Turn:")
                    if cpu.hand:
                        # Determine the most frequent rank in the CPU's hand
                        rank_counts = {card.rank: sum(1 for c in cpu.hand if c.rank == card.rank) for card in cpu.hand}
                        rank_to_ask = max(rank_counts, key=rank_counts.get)
                        print(f"{cpu.name} asks: Do you have any {rank_to_ask}s?")
                        game.player_ask_for_rank(cpu, human, rank_to_ask, is_cpu=True)
                    else:
                        print(f"{cpu.name} has no cards to play and skips the turn.")
            except Exception as e:
                print(f"An error occurred during the turn: {e}")
                continue  # Skip to the next turn if an error occurs

            turn += 1

        # End the game
        print("\nGame Over!")
        game.show_player_books()
        game.determine_winner()

    except RuntimeError as re:
        print(f"Game error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for playing Go Fish!")


# In[9]:


main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




