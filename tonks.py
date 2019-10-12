import deckOfCards 




def compare_all_hands():
    smallest_hand = 51
    tie_count = 0
    for player_hands in players:
        print( '%s has a hand of: '%(player_hands.name))
        player_hands.showHand()
        if player_hands.hand_value < smallest_hand:
            smallest_hand = player_hands.hand_value
            winner = player_hands.name
    for player_ties in players:
        if player_ties.hand_value == smallest_hand:
            tie_count += 1
    print(winner + " has the low hand with a total of " + str(smallest_hand))
    return [winner,tie_count]
    

def determine_higest_score():
    highest_total = 0
    for player in players:
        if player.game_total > highest_total:
            highest_total = player.game_total
    return highest_total

def intialize_new_round(players,deck):
    deck.create_deck()
    deck.shuffle()
    discard_pile.cards = []
    for player in range(len(players)):
        players[player].hand = []
        players[player].hand_value = 0
        for i in range(5):
            players[player].draw(deck)
    print('\n~~~~~~~Start of a new round!~~~~~~~\n')
        



deck = deckOfCards.Deck()
deck.create_deck()
deck.shuffle()

discard_pile = deckOfCards.Discard_Pile()

player_names = ['D', 'P', 'N']
players = [deckOfCards.Player(player_name) for player_name in player_names]


for player in players:
    for i in range(5):
        player.draw(deck)



breakpoint_total = int(input("How many total points would you like to play up until: "))
starting_position = 0
while determine_higest_score() < breakpoint_total:
    intialize_new_round(players, deck)
    round_over = False
    turn_counter = 0
    while  not round_over:
        for player in range(starting_position, len(players)):
            if turn_counter % len(players) == 0:
                print('\nStart of turn ' + str(turn_counter / len(players)+1))
            turn_counter += 1
            turn_over = False
            while not turn_over:
                print('\nIt is ' + players[player].name + "'s turn.")
                player_action = input("Call tonks('t') or draw('d') or show hand('s') or show scores('z'): ")
                if player_action == 't': 
                    starting_position = player
                    if turn_counter / len(players) + 1 > 0:
                        winner = compare_all_hands()
                        if not (winner[0] == players[player].name) or winner[1] > 1:
                            for all_hands in range(len(players)):
                                players[all_hands].hand_value = 0
                            players[player].hand_value = 30
                        else:
                            players[player].hand_value = 0
                        turn_over = True
                        round_over = True
                    else:
                        print("You cannot call tonks before turn 4")
                    
                elif player_action == 'd':
                    while players[player].discard_and_draw(deck,discard_pile) == True:
                        pass
                    turn_over = True
                elif player_action == 's':
                    players[player].showHand()
                elif player_action == 'z':
                    for player_name in range(len(players)):
                        print(players[player_name].name + ': ' 
                        + str(players[player_name].game_total), end = ' || ')
                else:
                    print('Enter a valid option')
                    
            if round_over:
                for player in players:
                    player.game_total += player.hand_value
                break
            starting_position = 0
    if determine_higest_score() >= breakpoint_total:
        print("Game Over")          


