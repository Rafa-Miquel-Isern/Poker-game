# Rafa Miquel
# Cards mini poker v.3

import random

#---------Class Defs -----------------------
class Card:
    def __init__(self, s, v):
        self.suit = s
        self.value = v
        if (v == 1):
            self.points = 14
        else:
            self.points = v
        
        # spades +0.4
        # hearts +0.3
        # diamonds +0.2
        # clubs +0.1
        if (s == "spades"):
            self.points = self.points + 0.4
        elif (s == "hearts"):
            self.points += 0.3
        elif (s == "diamonds"):
            self.points += 0.2
        elif (s == "clubs"):
            self.points += 0.1
        
    def display(self):
        if (self.suit == "spades"):
            print("[\u2660", self.value, "]", sep='')
        elif (self.suit == "hearts"):
            print("[\u2661", self.value, "]", sep='')
        elif (self.suit == "diamonds"):
            print("[\u2662", self.value, "]", sep='')
        elif (self.suit == "clubs"):
            print("[\u2663", self.value, "]", sep='')

    def __gt__(self, other):
        return self.points > other.points
        
class dice:

    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = random.randint(1, 4)
        
    def display_dice(self):
        print("===========Dice=============")
        print("The dice says:", self.value)
        
        if self.value == 1:
            print("Limit value 21")
        elif self.value == 2:
            print("Limit value 22")
        elif self.value == 3:
            print("Limit value 23")
        elif self.value == 4:
            print("Limit value 24")
                
        print("============================")
        
class Deck:
    def __init__(self):
        self.cards = [None] * 52
        #create each card object and insert into the array
        for i in range(13):
            self.cards[i] = Card("spades", i + 1)
        for i in range(13):
            self.cards[i + 13] = Card("hearts", i + 1)
        for i in range(13):
            self.cards[i + 26] = Card("diamonds", i + 1)
        for i in range(13):
            self.cards[i + 39] = Card("clubs", i + 1)
        
        self.cards2 = [None] * 52
        #create each card object and insert into the array
        for i in range(13):
            self.cards2[i] = Card("spades", i + 1)
        for i in range(13):
            self.cards2[i + 13] = Card("hearts", i + 1)
        for i in range(13):
            self.cards2[i + 26] = Card("diamonds", i + 1)
        for i in range(13):
            self.cards2[i + 39] = Card("clubs", i + 1)
          
        self.top1 = -1  
        self.top2 = -1
        
        self.deck_number = 1
        
        self.shuffle1()
        self.shuffle2()
        
    def shuffle1(self):
        for i in range(1000):
            idx1 = random.randint(0, len(self.cards) - 1)
            idx2 = random.randint(0, 51)
            
            temp = self.cards[idx1]
            self.cards[idx1] = self.cards[idx2]
            self.cards[idx2] = temp
            
    def shuffle2(self):
        for i in range(1000):
            idx3 = random.randint(0, len(self.cards2) - 1)
            idx4 = random.randint(0, 51)
            
            temp = self.cards2[idx3]
            self.cards2[idx3] = self.cards2[idx4]
            self.cards2[idx4] = temp
        
    def show(self):
        print("=============Deck1=================")
        for i in range(len(self.cards)):
            self.cards[i].display()
        print("===================================")
        
        print("=============Deck2=================")
        for i in range(len(self.cards2)):
            self.cards2[i].display()
        print("===================================")
    
    def dealCard(self):
        # return the card object that is at the top of the current deck
        if (self.deck_number == 1):
            if self.top1 + 1 < len(self.cards):  # verify if there are cards
                self.top1 += 1
                return self.cards[self.top1]
            else:
                return None  # if not, return none
        else:
            if self.top2 + 1 < len(self.cards2): # verify if there are cards
                self.top2 += 1
                return self.cards2[self.top2]
            else:
                return None
    
    def resetDeck(self):
        self.top1 = -1 
        self.shuffle1()
        
        self.top2 = -1 
        self.shuffle2()
        
class Player:
    def __init__(self, name, startingAmount):
        if name == "PC":
            self.name = "PC"
        else: 
            self.name = input("Who is playing?: ")
            
        self.hand = [] 
        self.numCards = 0
        self.wallet = startingAmount
        self.maxCards = 5
        self.total_points = 0
        
    def showPlayer(self):
        print("------", self.name, "------ $", self.wallet, sep="")
        for i in range(self.numCards):
            self.hand[i].display()
           
        
    def resetPlayer(self):
        self.numCards = 0
        self.hand = [] 
        self.total_points = 0
        
    def getCard(self, card):
        if self.numCards < self.maxCards:
           self.hand.append(card)
           self.numCards += 1
           self.total_points += card.points
        else:
           print("already has the limit of cards.")
       
    def score(self):
        score = max(card.points for card in self.hand)  # highest card score

        # Add bonus for Aces
        has_ace = any(card.value == 1 for card in self.hand)
        if has_ace:
            score += 1  # add 1 for Ace

        # Add bonus for same suit
        suits = [card.suit for card in self.hand]
        if len(set(suits)) == 1:  # All cards are from the same suit
            score += 1

        return score
        
    def __gt__(self, other):
        lScore = self.score()
        rScore = other.score()
        if lScore > rScore:
            return True
        else:
            return False

    def get_more_cards(self, deck, dice_value):
        
        while True:
            try:
                more = int(input("Do you want another card? (1. Yes, 2. No): "))
                if more == 1:
                    # Aquí pides una carta al mazo
                    card = deck.dealCard()
                    if card is not None:
                        self.getCard(card)  # Añade la carta a la mano
                        self.showPlayer()
                        if self.total_points > dice_value + 20:
                            print("¡Busted! over the limit.")
                            return True
                    else:
                        print("deck without cards.")
                        return True
                elif more == 2:
                    print("You decided not to take another card. Computer's Turn.")
                    card = deck.dealCard()
                    if card is not None:
                        pc.getCard(card)  # Asegúrate de pasar una carta al PC
                    else:
                        print("deck without cards.")
                    return False
                else:
                    print("Invalid option. Please select 1 or 2.")
            except ValueError:
                print("Please enter a valid number.")

    def pc_turn(self, deck, limit_value):
       
        print("------ PC's Turn ------")
        while self.numCards < self.maxCards:
            if self.total_points < limit_value - 2:  # Adjust PC logic to be more cautious
                card = deck.dealCard()
                if card is not None:
                    self.getCard(card)
                else:
                    print("The deck ran out of cards.")
                    break
            else:
                break
        print("End of PC's turn.")
          
#--------------------------------Main-----------------------------------------

myDeck = Deck()
myDeck.show()

user = Player(" ", 100)
pc = Player("PC", 999999999999999)

my_dice = dice()
my_dice.roll()
my_dice.display_dice()

while user.wallet > 0:
    user.resetPlayer()
    pc.resetPlayer()
    myDeck = Deck()  # Crear el objeto
    myDeck.resetDeck()
    
    print("==================================")
    print("You have $", user.wallet)
    
    while True:
        bet = int(input("Place a bet:"))
        if bet <= 0: 
            print("Invalid amount. Must be more than 0")
            continue
        if bet > user.wallet:
            print("You cannot bet more than your wallet!")
            continue
        user.wallet -= bet
        break

    user.getCard(myDeck.dealCard()) 
    pc.getCard(myDeck.dealCard()) 
    
    user.getCard(myDeck.dealCard()) 
    pc.getCard(myDeck.dealCard())
    
    user.showPlayer()  # muestra la mano del usuario
    pc.showPlayer()  # muestra la mano del PC
    
    print("Now it's your turn to decide if you want to take more cards.")
    
    if user.get_more_cards(myDeck, my_dice.value):
        print("You exceeded the limit and busted!")
        print("You lost the round.")
        continue

    print("Your score is",user.score())
    print("PC's score is", pc.score())
        
    if user.score() > pc.score():
        print("You win this round!")
        user.wallet += bet * 2
    else:
        print("PC wins this round!")
      
    my_dice.roll()
    my_dice.display_dice()

    print(f"Your wallet balance is: ${user.wallet}")

print("Game Over!")
