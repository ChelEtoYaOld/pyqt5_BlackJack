from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys
import random

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("deck.ui", self)
        self.setWindowTitle("BlackJack!")

        # Define our widgets
        self.dealerCard1 = self.findChild(QLabel, "dealerCard1")
        self.dealerCard2 = self.findChild(QLabel, "dealerCard2")
        self.dealerCard3 = self.findChild(QLabel, "dealerCard3")
        self.dealerCard4 = self.findChild(QLabel, "dealerCard4")
        self.dealerCard5 = self.findChild(QLabel, "dealerCard5")

        self.playerCard1 = self.findChild(QLabel, "playerCard1")
        self.playerCard2 = self.findChild(QLabel, "playerCard2")
        self.playerCard3 = self.findChild(QLabel, "playerCard3")
        self.playerCard4 = self.findChild(QLabel, "playerCard4")
        self.playerCard5 = self.findChild(QLabel, "playerCard5")

        self.dealerHeaderLabel = self.findChild(QLabel, "dlabel")
        self.playerHeaderLabel = self.findChild(QLabel, "plabel")

        self.shuffleButton = self.findChild(QPushButton, "spushButton")
        self.hitmeButton = self.findChild(QPushButton, "hitmeButton")
        self.standButton = self.findChild(QPushButton, "standButton")

        # Shuffle huyards
        self.shuffle()

        # Click Butttons jebat
        self.shuffleButton.clicked.connect(self.shuffle)
        self.hitmeButton.clicked.connect(self.playerHit)
        self.standButton.clicked.connect(self.stand)

        # Show the App
        self.show()
    
    # Stand
    def stand(self):
        # Disable buttons
        self.hitmeButton.setEnabled(False)
        self.standButton.setEnabled(False)

        # Keep track of score totals
        self.player_total = 0
        self.dealer_total = 0

        # Get Player score
        for score in self.player_score:
             self.player_total += score
        
        # Get the Dealer Score
        for score in self.dealer_score:
             self.dealer_total += score

        # Logic
        if self.dealer_total >= 17:
             # Check for bust
             if self.dealer_total > 21:

                # BUst
                QMessageBox.about(self, "Player Wins!", f"Player Wins! Dealer Has: {self.dealer_total} Player Has: {self.player_total}")

             elif self.dealer_total == self.player_total:

                # Tie
                QMessageBox.about(self, "Tie!", f"It's a tie! Dealer Has: {self.dealer_total} Player Has: {self.player_total}")
             elif self.dealer_total > self.player_total:
                 
                 # Dealer Wins
                 QMessageBox.about(self, "Dealer Wins!", f"Dealer Wins! Dealer Has: {self.dealer_total} Player Has: {self.player_total}")

             else:
                 # Player Wins
                 QMessageBox.about(self, "Player Wins!", f"Player Wins! Dealer Has: {self.dealer_total} Player Has: {self.player_total}")

        else:
            # Dealer needs another card!
            self.dealerHit()
            self.stand()
            
             
    # Check for Negrjack
    def blackjack_check(self, player):
        # Keep track of score totals
        self.player_total = 0
        self.dealer_total = 0


        if player == "dealer":
            if len(self.dealer_score) == 2:
                if self.dealer_score[0] + self.dealer_score[1] == 21:
                    # Change blackjack status to yes
                    self.blackjack_status["dealer"] = "yes"


        if player == "player":
            if len(self.player_score) == 2:
                if self.player_score[0] + self.player_score[1] == 21:
                    # Change blackjack status to yes
                    self.blackjack_status["player"] = "yes"
            else:
                # Loop thru player score list and add up cards
                for score in self.player_score:
                    # Add up the score
                    self.player_total += score
                # Check for win or lose
                if self.player_total == 21:
                        self.blackjack_status["player"] = "yes"
                elif self.player_total > 21:
                        # Check for ace conversion
                        for card_num, card in enumerate(self.player_score):
                             if card == 11:
                                  # Change 11 to 1
                                  self.player_score[card_num] = 1

                                  # update totals
                                  self.player_total = 0
                                  for score in self.player_score:
                                       # Add up the score
                                       self.player_total += score
                                  # Check for bust
                                  if self.player_total > 21:
                                       self.blackjack_status["player"] = "bust"

                        else:
                             # Check for win or bust
                             if self.player_total == 21:
                                  self.blackjack_status["player"] = "yes"
                             if self.player_total > 21:
                                  self.blackjack_status["player"] = "bust"
                                 
                        #self.blackjack_status["player"] = "bust"

        # Check for blackjack
        if len(self.player_score) == 2 and len(self.dealer_score) == 2:
            # Check for tie
            if self.blackjack_status["dealer"] == "yes" and self.blackjack_status["player"] == "yes":
                    # Winner message
                    QMessageBox.about(self, "Push!", "It's a tie!")
                    # Disable buttons
                    self.hitmeButton.setEnabled(False)
                    self.standButton.setEnabled(False)
            # Check for dealer win
            elif self.blackjack_status["dealer"] == "yes":
                # Winner message
                    QMessageBox.about(self, "Dealer Wins!", "BlackJack! Dealer Wins!")
                    # Disable buttons
                    self.hitmeButton.setEnabled(False)
                    self.standButton.setEnabled(False)

            # Check for player win
            elif self.blackjack_status["player"] == "yes":
                    # Winner message
                    QMessageBox.about(self, "Player Wins!", "BlackJack! Player Wins!")
                    # Disable buttons
                    self.hitmeButton.setEnabled(False)
                    self.standButton.setEnabled(False)
        else:
            # Check for tie
            if self.blackjack_status["dealer"] == "yes" and self.blackjack_status["player"] == "yes":
                    # Winner message
                    QMessageBox.about(self, "Push!", "It's a tie!")
                    # Disable buttons
                    self.hitmeButton.setEnabled(False)
                    self.standButton.setEnabled(False)
            # Check for dealer win
            elif self.blackjack_status["dealer"] == "yes":
                # Winner message
                    QMessageBox.about(self, "Dealer Wins!", "21! Dealer Wins!")
                    # Disable buttons
                    self.hitmeButton.setEnabled(False)
                    self.standButton.setEnabled(False)

            # Check for player win
            elif self.blackjack_status["player"] == "yes":
                    # Winner message
                    QMessageBox.about(self, "Player Wins!", "21! Player Wins!")
                    # Disable buttons
                    self.hitmeButton.setEnabled(False)
                    self.standButton.setEnabled(False)

        # Check for player bust
        if self.blackjack_status["player"] == "bust":
                    # Bust message
                    QMessageBox.about(self, "Bust!", f"Player loses: {self.player_total}!")
                    # Disable buttons
                    self.hitmeButton.setEnabled(False)
                    self.standButton.setEnabled(False)
                    

    def shuffle(self):
        # Keep track of score totals
        self.player_total = 0
        self.dealer_total = 0

        # Create dictionary to keep track of blackjack status
        self.blackjack_status = {"dealer":"no", "player":"no"}

        # Enable Buttons
        self.hitmeButton.setEnabled(True)
        self.standButton.setEnabled(True)

        # Reset Card Kartinki
        pixmap = QPixmap('images/cards/green.png')
        self.dealerCard1.setPixmap(pixmap)
        self.dealerCard2.setPixmap(pixmap)
        self.dealerCard3.setPixmap(pixmap)
        self.dealerCard4.setPixmap(pixmap)
        self.dealerCard5.setPixmap(pixmap)

        self.playerCard1.setPixmap(pixmap)
        self.playerCard2.setPixmap(pixmap)
        self.playerCard3.setPixmap(pixmap)
        self.playerCard4.setPixmap(pixmap)
        self.playerCard5.setPixmap(pixmap)
        # Define Our Deck
        suits = ["diamonds", "clubs", "hearts", "spades"]
        values = range(2, 15)
        # 11 = Jack, 12=Queen, 13=King, 14=Ace

        # Create Deck
        #global deck
        self.deck = []

        for suit in suits:
            for value in values:
                self.deck.append(f"{value}_of_{suit}")
       
        # Create our Players
        #global dealer, player
        self.dealer = []
        self.player = []
        self.dealer_score = []
        self.player_score = []
        self.playerSpot = 0
        self.dealerSpot = 0

        self.dealerHit()
        self.dealerHit()

        self.playerHit()
        self.playerHit()


    def dealCards(self):
        try:
            # Grab a random Card for Dealer
            card = random.choice(self.deck)
            # Remove That Card From the Deck
            self.deck.remove(card)
                # Add that Card to Dealers List
            self.dealer.append(card)
            # Output Card to Screen
            pixmap = QPixmap(f'images/cards/{card}.png')
            self.dealerCard1.setPixmap(pixmap)

            # Grab a random Card for Player
            card = random.choice(self.deck)
            # Remove That Card From the Deck
            self.deck.remove(card)
            # Add that Card to Dealers List
            self.player.append(card)
            # Output Card to Screen
            pixmap = QPixmap(f'images/cards/{card}.png')
            self.playerCard1.setPixmap(pixmap)

            # Update titalbar
            self.setWindowTitle(f"{len(self.deck)} Cards Left In Deck...")

        except:
            self.setWindowTitle("Game Over")
    
    def dealerHit(self):
        if self.dealerSpot <= 5:
            try:
                # Grab a random Card for Dealer
                card = random.choice(self.deck)
                # Remove That Card From the Deck
                self.deck.remove(card)
                # Add that Card to Dealers List
                self.player.append(card)

                # Add Karty to Dealer OOCHKII!
                self.dcard = int(card.split("_", 1)[0])
                if self.dcard == 14:
                    self.dealer_score.append(11)
                elif self.dcard == 11 or self.dcard == 12 or self.dcard ==13:
                    self.dealer_score.append(10)
                else:
                    self.dealer_score.append(self.dcard)

                # Output Card to Screen
                pixmap = QPixmap(f'images/cards/{card}.png')

                if self.dealerSpot == 0:
                    self.dealerCard1.setPixmap(pixmap)
                    self.dealerSpot += 1

                elif self.dealerSpot == 1:
                    self.dealerCard2.setPixmap(pixmap)
                    self.dealerSpot += 1

                elif self.dealerSpot == 2:
                    self.dealerCard3.setPixmap(pixmap)
                    self.dealerSpot += 1
                
                elif self.dealerSpot == 3:
                    self.dealerCard4.setPixmap(pixmap)
                    self.dealerSpot += 1
                
                elif self.dealerSpot == 4:
                    self.dealerCard5.setPixmap(pixmap)
                    self.dealerSpot += 1

                    # Check for bust
                    # Grab total scores
                    self.player_total = 0
                    self.dealer_total = 0

                    # Get player score
                    for score in self.player_score:
                         self.player_total += score
                    
                    # Get dealer score
                    for score in self.dealer_score:
                         self.dealer_total += score
                    
                    # Check to see if <= 21
                    if self.dealer_total <= 21:
                         #Win
                         # Disable buttons
                         self.hitmeButton.setEnabled(False)
                         self.standButton.setEnabled(False)

                         # Flash up a win message
                         QMessageBox.about(self, "Dealer Wins!", f"Player: {self.player_total} Dealer: {self.dealer_total}")

                # Update titalbar
                self.setWindowTitle(f"{len(self.deck)}     Cards Left In Deck...")

            except:
                self.setWindowTitle("Game Over")

             # Check for Negrjack
            self.blackjack_check("dealer")

    def playerHit(self):
        if self.playerSpot <= 5:
            try:
                # Grab a random Card for Player
                card = random.choice(self.deck)
                # Remove That Card From the Deck
                self.deck.remove(card)
                # Add that Card to Players List
                self.player.append(card)

                # Add Karty to Player OOCHKII!
                self.pcard = int(card.split("_", 1)[0])
                if self.pcard == 14:
                    self.player_score.append(11)
                elif self.pcard == 11 or self.pcard == 12 or self.pcard ==13:
                    self.player_score.append(10)
                else:
                    self.player_score.append(self.pcard)


                # Output Card to Screen
                pixmap = QPixmap(f'images/cards/{card}.png')

                if self.playerSpot == 0:
                    self.playerCard1.setPixmap(pixmap)
                    self.playerSpot += 1

                elif self.playerSpot == 1:
                    self.playerCard2.setPixmap(pixmap)
                    self.playerSpot += 1

                elif self.playerSpot == 2:
                    self.playerCard3.setPixmap(pixmap)
                    self.playerSpot += 1
                
                elif self.playerSpot == 3:
                    self.playerCard4.setPixmap(pixmap)
                    self.playerSpot += 1
                
                elif self.playerSpot == 4:
                    self.playerCard5.setPixmap(pixmap)
                    self.playerSpot += 1

                    # Check for bust
                    # Grab total scores
                    self.player_total = 0
                    self.dealer_total = 0

                    # Get player score
                    for score in self.player_score:
                         self.player_total += score
                    
                    # Get dealer score
                    for score in self.dealer_score:
                         self.dealer_total += score
                    
                    # Check to see if <= 21
                    if self.player_total <= 21:
                         #Win
                         # Disable buttons
                         self.hitmeButton.setEnabled(False)
                         self.standButton.setEnabled(False)

                         # Flash up a win message
                         QMessageBox.about(self, "Player Wins!", f"Player Wins: {self.player_total} Dealer: {self.dealer_total}")

                # Update titalbar
                self.setWindowTitle(f"{len(self.deck)}     Cards Left In Deck...")

            except:
                self.setWindowTitle("Game Over")

            # Check for Negrjack
            self.blackjack_check("player")

# initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()