

player_1={
    'player name' : input('Insert player 1 name: '),
    'health' : 100,
    'damage' : 10,
    'armor' : 50
}

player_2={
    'player name' : input('Insert player 2 name: '),
    'health' : 100,
    'damage' : 10,
    'armor' : 50
}

#function of attack of defender
def attack(attacker, defender):

    while defender['health'] != 0:

        if attacker['damage'] == 10:
            
            defender['health'] -= round((10 + (defender['armor'] / 
                                              defender['health']))) 
            defender['armor'] -= 5 
            print('{} health - {} '.format(defender['player name'],
                                        defender['health']))

        elif defender['health'] == 0:
            print(attacker['player name'] + ' win!')
            break

print(player_1['player name'] + ' vs ' + player_2['player name'])

attack(player_1, player_2)

