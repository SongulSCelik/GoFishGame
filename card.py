#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


class Card:
    SUIT_SYMBOLS = {
        'Hearts': '♥',
        'Diamonds': '♦',
        'Clubs': '♣',
        'Spades': '♠'
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        suit_symbol = self.SUIT_SYMBOLS[self.suit]
        return f"{self.rank} {suit_symbol}"

