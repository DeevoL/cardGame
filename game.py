import deckOfCards


deck = deckOfCards.Deck()
deck.createDeck()
deck.shuffle()

player1Name = input("Please enter in your name: ")
player1 = deckOfCards.Player(player1Name)

keepPlaying = True
while keepPlaying:
    yesOrNo = input(
        "Hi " 
        + player1Name 
        + ". Draw a card('y' or 'n')? Or Enter 's' to show hand: "
    )
                    
    if yesOrNo == 'y':
        (player1.draw(deck))
    elif yesOrNo == 's':
        player1.showHand()
        print('\n')
    elif yesOrNo == 'n':
        print("You are done drawing cards.")
        keepPlaying = False
    else:
        print("Please enter 'y' or 'n'")


    

    