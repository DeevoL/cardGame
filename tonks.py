import deckOfCards 




def compareAllHands():
    smallestHand = 51
    tieCount = 0
    for player in players:
        print( '%s has a hand of: '%(player.name))
        player.showHand()
        if player.handValue < smallestHand:
            smallestHand = player.handValue
            winner = player.name
    for player in players:
        if player.handValue == smallestHand:
            tieCount += 1
    print(winner + " has the low hand with a total of " + str(smallestHand))
    return [winner,tieCount]
    

def highestGameTotal():
    highestTotal = 0
    for player in players:
        if player.gameTotal > highestTotal:
            highestTotal = player.gameTotal
    return highestTotal

def initRound(players,deck):
    deck.createDeck()
    deck.shuffle()
    discardPile.cards = []
    for player in range(len(players)):
        players[player].hand = []
        players[player].handValue = 0
        for i in range(5):
            players[player].draw(deck)
    print('\n~~~~~~~Start of a new round!~~~~~~~\n')
        



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
startingPosition = 0
while highestGameTotal() < breakpointTotal:
    initRound(players, deck)
    roundOver = False
    turnCounter = 0
    while  not roundOver:
        for player in range(startingPosition, len(players)):
            if turnCounter % len(players) == 0:
                print('\nStart of turn ' + str(turnCounter / len(players)+1))
            turnCounter += 1
            turnOver = False
            while not turnOver:
                print('\nIt is ' + players[player].name + "'s turn.")
                playerAction = input("Call tonks('t') or draw('d') or show hand('s') or show scores('z'): ")
                if playerAction == 't': 
                    startingPosition = player
                    if turnCounter / len(players) + 1 > 3:
                        winner = compareAllHands()
                        if not (winner[0] == players[player].name or winner[1] > 1):
                            for allPlayers in range(len(players)):
                                players[allPlayers].handValue = 0
                            players[player].handValue = 30
                        else:
                            players[player].handValue = 0
                        turnOver = True
                        roundOver = True
                    else:
                        print("You cannot call tonks before turn 4")
                    
                elif playerAction == 'd':
                    while players[player].discardAndDraw(deck,discardPile) == True:
                        pass
                    turnOver = True
                elif playerAction == 's':
                    players[player].showHand()
                elif playerAction == 'z':
                    for playerName in range(len(players)):
                        print(players[playerName].name + ': ' 
                        + str(players[playerName].gameTotal), end = ' || ')
                else:
                    print('Enter a valid option')
                    playerAction = input("Call tonks('t') or draw('d') or show hand('s') or show scores('z'): ")
            if roundOver:
                for player in players:
                    player.gameTotal += player.handValue
                break
            startingPosition = 0
    if highestGameTotal() >= breakpointTotal:
        print("Game Over")          


