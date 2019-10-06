import deckOfCards 




def compareAllHands():
    smallestHand = 51
    for player in players:
        print( '%s has a hand of: '%(player.name))
        player.showHand()
        if player.handValue <= smallestHand:
            smallestHand = player.handValue
            winner = player.name
    print(winner + " has a lower hand with a total score of " + str(smallestHand))

def highestGameTotal():
    highestTotal = 0
    for player in players:
        if player.gameTotal > highestTotal:
            highestTotal = player.gameTotal
    return highestTotal

def initRound(players,deck):
    deck.createDeck()
    deck.shuffle()
    for player in range(len(players)):
        players[player].hand = []
        players[player].handValue = 0
        for i in range(5):
            players[player].draw(deck)
        



deck = deckOfCards.Deck()
deck.createDeck()
deck.shuffle()

discardPile = deckOfCards.Discard_Pile()

playerNames = ['D', 'P', 'N']
players = [deckOfCards.Player(playerName) for playerName in playerNames]


for player in players:
    for i in range(5):
        player.draw(deck)



breakpointTotal = int(input("How many total points would you like to play up until: "))

while highestGameTotal() < breakpointTotal:
    initRound(players, deck)
    roundOver = False
    while  not roundOver:
        print('\n~~~~~~~Start of a new round!~~~~~~~\n')
        for player in range(len(players)):
            turnOver = False
            while not turnOver:
                print("It is " + players[player].name + "'s turn.")
                playerAction = input("Call tonks('t') or draw('d') or show hand('s'): ")
                if playerAction == 't':
                    compareAllHands()
                    turnOver = True
                    roundOver = True
                    
                elif playerAction == 'd':
                    while players[player].discardAndDraw(deck,discardPile) == True:
                        pass
                    turnOver = True
                elif playerAction == 's':
                    players[player].showHand()
                else:
                    print('Enter a valid option')
                    playerAction = input("Call tonks('t') or draw('d') or show hand('s'): ")
            if roundOver:
                for player in players:
                    player.gameTotal += player.handValue
                break
    if highestGameTotal() >= breakpointTotal:
        print("Game Over")          


