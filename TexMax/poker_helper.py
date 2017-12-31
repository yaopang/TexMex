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
# Include all cards related functionalities:
# card_ranks: return rank of each card
# allmax: return hand with highest rank from a list of hands
# win_hand: return a list of winning hands
# hand_rank: return numerical representation of a hand of cards
#               straight flush: (8 + rank of the highest card)
#               4 of a kind: (7 + rank of the quartet + rank of the remaining card)
#               full house: (6 + rank of the trio + rank of the pair)
#               flush: (5 + rank of all cards)
#               straight: (4 + rank of the highest card)
#               3 of a kind: (3 + rank of the trio + rank of the remaining card)
#               2 pairs: (2 + rank of two pairs + rank of the remaining card)
#               1 pair : (1 + rank of the pair + rank of the remaing card)
#               high card: (0 + rank of all cards)
# all the other functions are utilities functions to determine hand


import itertools
import random


def card_ranks(cards):
    ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks   #Ace low straight

def allmax(iterable, key = None):
    result = [i for i in iterable if hand_rank(i) == hand_rank(max(iterable, key = key or (lambda x: x)))]
    return result[0] if len(result) == 1 else result

def win_hand(hands):
    return allmax(hands, key = hand_rank)

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind (2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pairs (ranks):
        return (2, two_pairs(ranks), ranks)
    elif kind (2, ranks):
        return(1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def best_hand(hand):
    all_comb = itertools.combinations(hand, 5) #generate all permutation with 5 out of 7 cards
    max_hand = list(max(all_comb, key = hand_rank))
    max_hand.sort(reverse=True)
    return max_hand


def kind(n, ranks):
    for i in ranks:
        if ranks.count(i) == n:
            return i
    return None


def two_pairs(ranks):
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None


def straight(ranks):
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


