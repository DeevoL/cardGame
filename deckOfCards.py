import random


class Deck:

    def __init__(self):
        self.cards = []
        self.createDeck()

    def createDeck(self):
        self.cardValues = [
            ['A', 1], 
            ['2', 2], 
            ['3', 3],
            ['4', 4], 
            ['5', 5], 
            ['6', 6],
            ['7', 7], 
            ['8', 8], 
            ['9', 9], 
            ['10', 10], 
            ['J', 10],  
            ['Q', 10], 
            ['K', 10]
            ]
        
        suits = ["\u2665", "\u2663", "\u2666", "\u2660"]
        
        self.cards = [
            (cardValue, suit) 
            for cardValue in self.cardValues 
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
        invalidInput = True
        while invalidInput:
            try:
                cardsToDiscard = input("Which card(s) would you like to drop? ").split(' ')
                discardList = [int(card) for card in cardsToDiscard]
                invalidInput = False
            except:
                print("Enter a single number or multiple numbers seperated by a space.")
                invalidInput = True
        
        if len(discardList) == 1:
            self.handValue -= self.hand[(discardList[0]-1)][0][1] 
            self.hand.pop(discardList[0]-1)
            self.hand.append(deck.drawCard())
            self.handValue += self.hand[(len(self.hand))-1][0][1]
            return False
        elif len(discardList) > 1:
            dontDraw = False
            discardList.sort(reverse = True)
            faceValue = self.hand[(discardList[0]-1)][0][0]
            suitValue = self.hand[(discardList[0]-1)][1]
            if not all(self.hand[cardPosition-1][0][0] == faceValue 
                       for cardPosition in discardList
            ):
                if all(self.hand[cardPosition-1][1] == suitValue 
                       for cardPosition in discardList
                ):
                    sortedDiscardFaces = [self.hand[i-1][0][0] for i in discardList]
                    indexesOfFaces = []
                    for subList in deck.cardValues:
                        for face in sortedDiscardFaces:
                            if face in subList:
                                indexesOfFaces.append(deck.cardValues.index(subList))
                    indexesOfFaces.sort()
                
                    for n in indexesOfFaces[:len(indexesOfFaces)-1]:
                        for x in range(1, len(indexesOfFaces)):
                            if not(int(n + 1) == int(indexesOfFaces[x])):
                                dontDraw = True
                else:
                    dontDraw = True                    
             
            if not dontDraw:            
                for cardPosition in discardList:
                    self.handValue -= self.hand[cardPosition-1][0][1]
                    self.hand.pop(cardPosition-1)
                self.hand.append(deck.drawCard())
                self.handValue += self.hand[(len(self.hand))-1][0][1]
                return False
            else:
                print("This is not a valid combo. Try again.")
                return True
            
