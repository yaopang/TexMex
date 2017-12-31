'''
Created on Dec 6,2017

@author: Shengyao Guo, Wenhao Sheng
'''
#  Pthyon 3.6.2
#  PyQt 5.6
# -----------
# User Instructions
#
# Utility function:
# Include all deck related functionalities: shuffle, draw, and remove

import random
def get_deck():
    deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
    return deck

def draw_deck(deck):
    random.shuffle(deck)
    card = deck.pop(0)
    return card

def remove_deck(deck, card):
    deck.remove(card)
    return