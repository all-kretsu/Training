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

def attack(attacker, defender):	

	while defender['health'] != 0:

		if attacker['damage'] == 10:

			defender['health'] -= (10 + (defender['armor'] / 
                                        defender['health'])) 
            defender['armor'] -= 5

			print('{} health - {} '.format(player_2['player name'],
										   player_2['health']))
			if defender['health'] == 0:
				print(attacker['player name'] + ' win!')
				break
			continue


print(player_1['player name'] + ' vs ' + player_2['player name'])

attack(player_1, player_2)
