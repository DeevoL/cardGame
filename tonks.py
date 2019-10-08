import deckOfCards 




def compare_all_hands():
    smallest_hand = 51
    tie_count = 0
    for player_hands in players:
        print( '%s has a hand of: '%(player_hands.name))
        player_hands.showHand()
        if player_hands.handValue < smallest_hand:
            smallest_hand = player_hands.handValue
            winner = player_hands.name
    for player_ties in players:
        if player_ties.handValue == smallest_hand:
            tie_count += 1
    print(winner + " has the low hand with a total of " + str(smallest_hand))
    return [winner,tie_count]
    

def determine_higest_score():
    highestTotal = 0
    for player in players:
        if player.gameTotal > highestTotal:
            highestTotal = player.gameTotal
    return highestTotal

def intialize_new_round(players,deck):
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
while determine_higest_score() < breakpointTotal:
    intialize_new_round(players, deck)
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
                player_action = input("Call tonks('t') or draw('d') or show hand('s') or show scores('z'): ")
                if player_action == 't': 
                    startingPosition = player
                    if turnCounter / len(players) + 1 > 0:
                        winner = compare_all_hands()
                        if not (winner[0] == players[player].name) or winner[1] > 1:
                            for all_hands in range(len(players)):
                                players[all_hands].handValue = 0
                            players[player].handValue = 30
                        else:
                            players[player].handValue = 0
                        turnOver = True
                        roundOver = True
                    else:
                        print("You cannot call tonks before turn 4")
                    
                elif player_action == 'd':
                    while players[player].discardAndDraw(deck,discardPile) == True:
                        pass
                    turnOver = True
                elif player_action == 's':
                    players[player].showHand()
                elif player_action == 'z':
                    for playerName in range(len(players)):
                        print(players[playerName].name + ': ' 
                        + str(players[playerName].gameTotal), end = ' || ')
                else:
                    print('Enter a valid option')
                    
            if roundOver:
                for player in players:
                    player.gameTotal += player.handValue
                break
            startingPosition = 0
    if determine_higest_score() >= breakpointTotal:
        print("Game Over")          


