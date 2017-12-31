'''
Created on Dec 6,2017

@author: Shengyao Guo, Wenhao Sheng
'''
#  Pthyon 3.6.2
#  PyQt 5.6
# -----------
# User Instructions
#
# Icons at the top tool bar (left to right):
# Exit:    exit the program
# Reset:   reset the table, two cards in hand, three card on the table
# Deal:    deal one random card from the remaining deck to the table when there are less than five cards on the table
#
# Top left section shows cards in hand, always two cards
# Top right section shows the best cards combining the cards in hand and cards on the table
# Mid section shows cards on the table, can be three to five cards
# Bottom section shows hand rankings and corresponding probabilities given cards on the table and in hand.
# If cards can form two or more types of hand, the probabilites only consider the hand with the highest hand rank.
# eg, K Q Q Q J 10 9 will be considered as straight instead of 3 of a kind
# User can manage the risk and adjust their gambling strategy based on the probabilities.
# ----------
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from deck import *
from poker_helper import *
from hand_probability import *
import operator

class Example(QMainWindow):
    hand_names = ['straight flush', '4 of a kind', 'full house', 'flush', 'straight', '3 of a kind', '2 pairs',
                  '1 pair', 'high card']
    suits = ['♥','♦','♣','♠']
    def __init__(self):
        super().__init__()
        self.initUI()

    #Convert Cards To Corresponding Ranks And Suits
    def show_card(self, cardWidget, card):
        card = card.replace('T', '10')
        card = card.replace('H', '♥')
        card = card.replace('D', '♦')
        card = card.replace('C', '♣')
        card = card.replace('S', '♠')
        if card[-1] == '♥' or card[-1] == '♦':
            cardWidget.setStyleSheet("color: red;")
        else:
            cardWidget.setStyleSheet("color: black;")
        return card

    def set_besthand(self):
        if self.table_card_count >= 3:
            hand = best_hand(self.cards)
            hand_name = self.hand_names[8-hand_rank(hand)[0]]
            self.bestname.setText(hand_name)
            for i in range(len(hand)):
                cmd = 'self.besthand%d.setText(self.show_card(self.besthand%d, hand[%d]))' % (
                i, i, i)
                exec(cmd)

    def set_prob(self):
        self.probWidget.setStyleSheet("color: black;")
        probs = hand_probability(self.cards, self.deck)
        max_key = max(probs.items(), key=operator.itemgetter(1))[0]
        if max_key == 'straight flush':
            self.probWidget = self.P_RF
        elif max_key =='4 of a kind':
            self.probWidget = self.P_SF
        elif max_key == 'full house':
            self.probWidget = self.P_FK
        elif max_key == 'flush':
            self.probWidget = self.P_FH
        elif max_key == 'straight':
            self.probWidget = self.P_FL
        elif max_key == '3 of a kind':
            self.probWidget = self.P_ST
        elif max_key == '2 pairs':
            self.probWidget = self.P_TK
        elif max_key == '1 pair':
            self.probWidget = self.P_TP
        else:
            self.probWidget = self.P_OP
        self.probWidget.setStyleSheet("color: red;")
        self.P_RF.setText("%.2f" %probs['straight flush'] + " % ")
        self.P_SF.setText("%.2f" %probs['4 of a kind'] + " % ")
        self.P_FK.setText("%.2f" %probs['full house'] + " % ")
        self.P_FH.setText("%.2f" %probs['flush'] + " % ")
        self.P_FL.setText("%.2f" %probs['straight'] + " % ")
        self.P_ST.setText("%.2f" %probs['3 of a kind'] + " % ")
        self.P_TK.setText("%.2f" %probs['2 pairs'] + " % ")
        self.P_TP.setText("%.2f" %probs['1 pair'] + " % ")
        self.P_OP.setText("%.2f" %probs['high card'] + " % ")
        return

    #Define Exit Event (Triggered When Exit Buttion Is Clicked)
    def exit_event(self):
        qApp.quit

    #Define Refresh Event (Triggered When App Is Initialized or Refresh Button Is Clicked)
    def refresh_event(self):
        self.deck = get_deck()
        self.table_card_count = 3
        self.cards = []
        for i in range(5):
            c = draw_deck(self.deck)
            self.cards.append(c)
        self.hand0.setText(self.show_card(self.hand0,self.cards[0]))
        self.hand1.setText(self.show_card(self.hand1,self.cards[1]))
        self.table0.setText(self.show_card(self.table0,self.cards[2]))
        self.table1.setText(self.show_card(self.table1,self.cards[3]))
        self.table2.setText(self.show_card(self.table2,self.cards[4]))
        self.table3.setText('')
        self.table4.setText('')
        self.bestname.setText('')
        self.besthand0.setText('')
        self.besthand1.setText('')
        self.besthand2.setText('')
        self.besthand3.setText('')
        self.besthand4.setText('')
        self.P_RF.setText('')
        self.P_SF.setText('')
        self.P_FK.setText('')
        self.P_FH.setText('')
        self.P_FL.setText('')
        self.P_ST.setText('')
        self.P_TK.setText('')
        self.P_TP.setText('')
        self.P_OP.setText('')
        self.set_besthand()
        self.set_prob()

    #Define Deal Event (Trigged When Deal Button Is Clicked)
    def deal_event(self):
        if self.table_card_count >= 5:
            return
        c = draw_deck(self.deck)
        self.cards.append(c)
        cmd = 'self.table%d.setText(self.show_card(self.table%d, c))' %(self.table_card_count,self.table_card_count)
        exec(cmd)
        self.table_card_count += 1
        self.set_besthand()
        self.set_prob()
        return

    def initUI(self):

        #General Setup
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('TexMax (Texas Poker Simulator)')


        #Cards Placeholder Setup
        self.hand0 = QLabel('',self)
        self.hand1 = QLabel('', self)
        self.table0 = QLabel('',self)
        self.table1 = QLabel('',self)
        self.table2 = QLabel('',self)
        self.table3 = QLabel('',self)
        self.table4 = QLabel('',self)
        self.bestname = QLabel('', self)
        self.besthand0 = QLabel('', self)
        self.besthand1 = QLabel('', self)
        self.besthand2 = QLabel('', self)
        self.besthand3 = QLabel('', self)
        self.besthand4 = QLabel('', self)

        # Label Setup
        lb_hand = QLabel('Hand', self)
        lb_table = QLabel('Table', self)
        lb_besthand = QLabel('Best hand', self)
        lb_analysis = QLabel('Analysis', self)
        lb_RF = QLabel('Straight flush:', self)
        self.P_RF = QLabel('', self)
        lb_SF = QLabel('Four of a kind:', self)
        self.P_SF = QLabel('', self)
        lb_FK = QLabel('Full house:', self)
        self.P_FK = QLabel('', self)
        lb_FH = QLabel('Flush:', self)
        self.P_FH = QLabel('', self)
        lb_FL = QLabel('Straight:', self)
        self.P_FL = QLabel('', self)
        lb_ST = QLabel('Three of a kind:', self)
        self.P_ST = QLabel('', self)
        lb_TK = QLabel('Two pairs:', self)
        self.P_TK = QLabel('', self)
        lb_TP = QLabel('One pair:', self)
        self.P_TP = QLabel('', self)
        lb_OP = QLabel('High card:', self)
        self.P_OP = QLabel('', self)
        self.probWidget = self.P_FH

        # Toolbar Setup
        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        exitAct.triggered.connect(qApp.quit)

        refreshAct = QAction(QIcon('refresh.png'), 'Refresh', self)
        refreshAct.triggered.connect(self.refresh_event)

        dealAct = QAction(QIcon('deal.png'), 'Deal', self)
        dealAct.triggered.connect(self.deal_event)

        self.toolbar = self.addToolBar('toolbar')
        self.toolbar.addAction(exitAct)
        self.toolbar.addAction(refreshAct)
        self.toolbar.addAction(dealAct)

        lb_hand.setGeometry(50,50,50,50)
        self.hand0.setGeometry(50,100,50,50)
        self.hand1.setGeometry(100,100,50,50)
        lb_besthand.setGeometry(200,27.5,100,100)
        self.bestname.setGeometry(300,27.5,100,100)
        self.besthand0.setGeometry(200,100,50,50)
        self.besthand1.setGeometry(250,100,50,50)
        self.besthand2.setGeometry(300,100,50,50)
        self.besthand3.setGeometry(350,100,50,50)
        self.besthand4.setGeometry(400,100,50,50)
        lb_table.setGeometry(50,150,50,50)
        self.table0.setGeometry(50,200,50,50)
        self.table1.setGeometry(100,200,50,50)
        self.table2.setGeometry(150, 200,50,50)
        self.table3.setGeometry(200,200,50,50)
        self.table4.setGeometry(250,200,50,50)
        lb_analysis.setGeometry(50,250,50,50)
        lb_RF.setGeometry(50,300,100,50)
        self.P_RF.setGeometry(150,300,50,50)
        lb_SF.setGeometry(50,350,100,50)
        self.P_SF.setGeometry(150, 350, 50, 50)
        lb_FK.setGeometry(50, 400, 100, 50)
        self.P_FK.setGeometry(150, 400, 50, 50)
        lb_FH.setGeometry(200, 300, 100, 50)
        self.P_FH.setGeometry(300, 300, 50, 50)
        lb_FL.setGeometry(200, 350, 100, 50)
        self.P_FL.setGeometry(300, 350, 50, 50)
        lb_ST.setGeometry(200, 400, 100, 50)
        self.P_ST.setGeometry(300, 400, 50, 50)
        lb_TK.setGeometry(350, 300, 100, 50)
        self.P_TK.setGeometry(450, 300, 50, 50)
        lb_TP.setGeometry(350, 350, 100, 50)
        self.P_TP.setGeometry(450, 350, 50, 50)
        lb_OP.setGeometry(350, 400, 100, 50)
        self.P_OP.setGeometry(450, 400, 50, 50)

        # Initialize Content
        self.refresh_event()

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())