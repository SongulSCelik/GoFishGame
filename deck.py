#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import random
from card import Card

class Deck:
    def __init__(self):
        suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards

