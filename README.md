# TexMex
A Texas Poker Simulator

## Abstract
Our work provides a simulator for the famous Texas Hold’em poker game along with a probability estimator which shows the probability of getting any types of hand. 
With the help of our probability estimator, players could adjust their gambling strategies to maximize their beneﬁt.

## 1.Example

### 1.1.Hole cards and the ﬂop 

We are going to demonstrate how our program works by an example. We are dealing with a deck of 52 cards. The image shown in ﬁgure 1 is the initial state of our program. There are three buttons on the top left corner. The red cross gives you the option to exit from the program. The middle button is the refresh button, which will shufﬂe the deck, and draw another sets of cards. The rightmost button is used to simulate ’drawing card from the top of the deck’. In this initial state, there are two cards, which are also known as the ’hole cards’. These two cards are drawn face down to the player. After hitting the refresh button, we are able to generate a new set of hole cards. The table section consists of a series of three cards, which are also known as ’the ﬂop’. We are assuming that the player will not fold at this stage. Under the ’best hand’ section is the best hand that the player can have so far. In the example, the player’s best hand so far is high card. Note that the series of cards has already been assorted in ascending order. Finally, under the analysis part, we have the probability of getting a certain hand as the player decides to play on. The type of hand with the highest probability is marked in red. This feature will give the player a guide of whether it is beneﬁcial to play on. 
