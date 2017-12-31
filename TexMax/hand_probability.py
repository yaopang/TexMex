''''
Created on Dec 6,2017

@author: Shengyao Guo, Wenhao Sheng
'''
#  Pthyon 3.6.2
#  PyQt 5.6
# -----------
# User Instructions
#
# Utility function:
# hand_probability: return probablity of each hand
# _


from poker_helper import *
from deck import *
import itertools

hand_names = ['straight flush', '4 of a kind', 'full house', 'flush', 'straight', '3 of a kind', '2 pairs',
              '1 pair', 'high card']
def hand_probability(hand, deck):
        comb = itertools.combinations(deck, 7 - len(hand))
        counts = dict([(key, 0) for key in hand_names])
        for i in comb:
            i = list(i)
            all_comb = itertools.combinations(i + hand, 5)  # generate all comination with 5 out of 7 cards
            max_hand = max(all_comb, key=hand_rank)
            rank = hand_rank(max_hand)[0]

            if rank == 8:
              counts['straight flush'] += 1
            elif rank == 7:
                counts['4 of a kind'] += 1
            elif rank == 6:
                counts['full house'] += 1
            elif rank == 5:
                counts['flush'] += 1
            elif rank == 4:
                counts['straight'] += 1
            elif rank == 3:
                counts['3 of a kind'] += 1
            elif rank == 2:
                counts['2 pairs'] += 1
            elif rank == 1:
                counts['1 pair'] += 1
            else:
                counts['high card'] += 1

        factor = 1.0 / sum(counts.values())   #normalize counts to probability
        for key in counts:
            counts[key] = counts[key] * factor * 100

        return counts


