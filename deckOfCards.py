import random


class Deck:

    def __init__(self):
        self.cards = []
        self.createDeck()

    def createDeck(self):
        cardValues = [
            ('A', 1), 
            ('2', 2), 
            ('3', 3),
            ('4', 4), 
            ('5', 5), 
            ('6', 6),
            ('7', 7), 
            ('8', 8), 
            ('9', 9), 
            ('10', 10), 
            ('J', 10),  
            ('Q', 10), 
            ('K', 10)
            ]
        suits = ["\u2665", "\u2663", "\u2666", "\u2660"]
        
        self.cards = [
            (cardValue, suit) 
            for cardValue in cardValues 
            for suit in suits
            ]
    
    def printDeck(self):
        print(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)
    
    def drawCard(self):
        return self.cards.pop()
        
        

class Card:

    def __init__(self, face, suit, value):
        self.value = value
        self.suit = suit
        self.face = face


class Player:

    def __init__(self,name):
        self.name = name
        self.hand = []
        self.handValue = 0

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        self.handValue += self.hand[(len(self.hand))-1][0][1] 
        return self
        
    def showHand(self):
        for i in range(len(self.hand)): 
            print(self.hand[i][0][0] + self.hand[i][1])
        print("Total: " + str(self.handValue))

    def discardAndDraw(self,deck):
        cardsToDiscard = input("Which card(s) would you like to drop? ").split(' ')
        discardList = [int(card) for card in cardsToDiscard]
        if len(discardList) == 1:
            self.handValue -= self.hand[(discardList[0]-1)][0][1] 
            self.hand.pop(discardList[0]-1)
            self.hand.append(deck.drawCard())
            self.handValue += self.hand[(len(self.hand))-1][0][1]
            return False
        elif len(discardList) > 1:
            discardList.sort(reverse = True)
            pairvalue = self.hand[(discardList[0]-1)][0][1]
            for cardPosition in discardList:
                if not (self.hand[cardPosition-1][0][1] == pairvalue):
                    print("This is not a valid combo. Try again.")
                    break
                else:
                    for cardPosition in discardList:
                        self.handValue -= self.hand[cardPosition-1][0][1]
                        self.hand.pop(cardPosition-1)
                        
            self.hand.append(deck.drawCard())
            self.handValue += self.hand[(len(self.hand))-1][0][1]
            return False
            
