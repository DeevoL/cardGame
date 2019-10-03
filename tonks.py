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


deck = deckOfCards.Deck()
deck.createDeck()
deck.shuffle()

playerNames = ['D']
players = [deckOfCards.Player(playerName) for playerName in playerNames]


for player in players:
    for i in range(5):
        player.draw(deck)

compareAllHands()

while True:
    if players[0].discardAndDraw(deck) == False:
        break

players[0].showHand()

