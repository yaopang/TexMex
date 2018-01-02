# TexMex
A Texas Poker Simulator
## Author
Shengyao Guo     <br />   s8guo@eng.ucsd.edu

## Abstract
Our work provides a simulator for the famous Texas Hold’em poker game along with a probability estimator which shows the probability of getting any types of hand. 
With the help of our probability estimator, players could adjust their gambling strategies to maximize their beneﬁt.

## 1.Example

### 1.1.Hole cards and the ﬂop 

We are going to demonstrate how our program works by an example. We are dealing with a deck of 52 cards. The image shown in ﬁgure 1 is the initial state of our program. There are three buttons on the top left corner. The red cross gives you the option to exit from the program. The middle button is the refresh button, which will shufﬂe the deck, and draw another sets of cards. The rightmost button is used to simulate ’drawing card from the top of the deck’. In this initial state, there are two cards, which are also known as the ’hole cards’. These two cards are drawn face down to the player. After hitting the refresh button, we are able to generate a new set of hole cards. The table section consists of a series of three cards, which are also known as ’the ﬂop’. We are assuming that the player will not fold at this stage. Under the ’best hand’ section is the best hand that the player can have so far. In the example, the player’s best hand so far is high card. Note that the series of cards has already been assorted in ascending order. Finally, under the analysis part, we have the probability of getting a certain hand as the player decides to play on. The type of hand with the highest probability is marked in red. This feature will give the player a guide of whether it is beneﬁcial to play on. 


### 1.2.The turn 
After the initial state, if the player feels like he is in a good shape and decides top lay on, an additional single card will be drawn from the deck. As a new card is added, our program will re-calculate the best hand and the probabilities. As shown in ﬁgure 2, an spade 3 is drawn, and now the best hand is one pair. And this proves that the prediction that we made in the previous state is right.

### 1.3.The river 
The ﬁnal card is drawn in this state. After this, the game issettled. Our program will not do more predictions. It will only return the best hand of ﬁve cards chosen from the ﬁve cards on the table and the two hole cards. In our example, the player will end up with a one pair. 

## 2.Method
To get the probability analysis, we have to consider all the possible hands we might get. When our program is in its initial state, there are only 3 cards on the table. And, every card in the deck may be drawn with the same probability. Hence, we have to consider (47 choose 2) possibilities. For every possible 7-card series, we will run our algorithm ‘handprobability.py’ to ﬁnd out the best 5-card series of the 7 cards to choose from. Finally, we will add up the number of possible hands for each hand type. Dividing the those numbers by the number of all possible hands will give us the probability of getting a speciﬁc type of hand in the end. 

