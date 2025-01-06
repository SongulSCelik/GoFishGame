#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


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

