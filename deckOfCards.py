import random


class Deck:

    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        self.card_values = [
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
            (card_value, suit) 
            for card_value in self.card_values 
            for suit in suits
            ]
    
    def print_deck(self):
        print(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self):
        return self.cards.pop()
        
        

class Card:

    def __init__(self, face, suit, value):
        self.value = value
        self.suit = suit
        self.face = face

class Discard_Pile:

    def __init__(self):
        self.cards = []

    def print_pile(self):
        if len(self.cards) > 0: 
            print("Discard Pile: ", end = '') 
            for i in range(len(self.cards) ):
                print(self.cards[-i][0][0] + self.cards[-i][1], end = ' ')
                if i == len(self.cards)-1:
                    print('\n')

class Player:

    def __init__(self,name):
        self.name = name
        self.hand = []
        self.hand_value = 0
        self.game_total = 0

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        self.hand_value += self.hand[(len(self.hand))-1][0][1] 
        return self
        
    def show_hand(self):
        for i in range(len(self.hand)): 
            print(self.hand[i][0][0] + self.hand[i][1])
        print("Total: " + str(self.hand_value))

    def discard_and_draw(self,deck,discard_pile):
        invalid_input = True
        discard_pile.print_pile()
        self.show_hand()
        draw_choice = 1
        
        while invalid_input:
            try:
                cards_to_discard = input("Which card(s) would you like to drop? ").split(' ')
                discard_list = [int(card) for card in cards_to_discard]
                invalid_input = False
            except:
                print("Enter a single number or multiple numbers seperated by a space.")
                invalid_input = True
            
            if len(discard_pile.cards) > 0:
                draw_choice = input("Would you like to draw from the deck(1) or pile(2)? ")
                if int(draw_choice) == 2 and len(discard_pile.cards) > 1:
                    pile_choice = input("Which card in the pile? ")
            
        if len(discard_list) == 1:
            temp_pile = discard_pile.cards
            self.hand_value -= self.hand[(discard_list[0])-1][0][1] 
            discard_pile.cards = []
            discard_pile.cards.append(self.hand.pop(discard_list[0]-1))
            print("Discard pile: " +discard_pile.cards[0][0][0] + discard_pile.cards[0][1])
            if int(draw_choice) == 1:
                self.hand.append(deck.draw_card())
            else:
                self.hand.append(temp_pile[0])
            self.hand_value += self.hand[(len(self.hand))-1][0][1]
            return False
        elif len(discard_list) > 1:
            dont_draw = False
            discard_list.sort(reverse = True)
            face_value = self.hand[(discard_list[0]-1)][0][0]
            suit_value = self.hand[(discard_list[0]-1)][1]
            if not all(self.hand[card_position-1][0][0] == face_value 
                       for card_position in discard_list) and len(discard_list) > 2:
                if all(self.hand[card_position-1][1] == suit_value 
                       for card_position in discard_list):
                    sorted_discard_faces = [self.hand[i-1][0][0] for i in discard_list]
                    indexes_of_faces = []
                    for sublist in deck.card_values:
                        for face in sorted_discard_faces:
                            if face in sublist:
                                indexes_of_faces.append(deck.card_values.index(sublist))
                    indexes_of_faces.sort()
                    x = 1
                    for n in indexes_of_faces[:len(indexes_of_faces)-1]:
                        if not(int(n + 1) == int(indexes_of_faces[x])):
                                dont_draw = True
                        x += 1
                else:
                    dont_draw = True                    
            elif all(self.hand[card_position-1][0][0] == face_value 
                       for card_position in discard_list):
                dont_draw = False
            else:
                dont_draw = True 
            if not dont_draw:            
                temp_pile = discard_pile.cards[::]
                discard_pile.cards = []
                for card_position in discard_list:
                    self.hand_value -= self.hand[card_position-1][0][1]
                    discard_pile.cards.append(self.hand.pop(card_position-1))
                    
                discard_pile.print_pile()
                if int(draw_choice) == 1:
                    self.hand.append(deck.draw_card())
                elif len(temp_pile) == 1:
                    self.hand.append(temp_pile[0])
                else:
                    self.hand.append(temp_pile[int(pile_choice)])
                self.hand_value += self.hand[(len(self.hand))-1][0][1]
                return False
            else:
                print("This is not a valid combo. Try again.")
                return True
            
