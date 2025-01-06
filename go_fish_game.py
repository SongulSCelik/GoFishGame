#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


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
            
            
    

