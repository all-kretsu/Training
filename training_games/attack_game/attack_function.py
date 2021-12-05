import math

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

def attack_func(damage, damage_int, health,
                health_int, armor, armor_int):

    while health != 0:
        if damage == damage_int:
            health_rest = round(health_int + (armor / health))
            health_rest = math.fabs(health_rest)
            health -= health_rest
            armor -= armor_int

        print('{} health - {} '.format(player_2['player name'],
                                            health))

attack_func(player_1['damage'], 10, player_2['health'],
                        10, player_2['armor'], 5)
