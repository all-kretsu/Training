# its a training file
import random


# creating warrior class
class Warrior():
    def __init__(self, turn, attack=100, health=100):
        self.attack = attack
        self.health = health
        self.turn = turn

# create example class
unite_1 = Warrior(0, 100)
unite_2 = Warrior(1, 100)

while unite_1.health or unite_2.health <= 0:
    player_attack = random.randint(0,1)
    if player_attack == unite_1.turn:
        print('\nUnite 1 attack:')
        if random.randint(0, 5) == 1:
            print('\tSuper Hit!')
            unite_2.health -= 20
        unite_2.health -= unite_1.attack / 10
        print('\nUnite 2:')
        print(unite_2.health)
        if unite_2.health == 0.0:
            break
    elif player_attack == unite_2.turn:
        print('\nUnite 2 attack:')
        if random.randint(0, 5) == 1:
                print('\tSuper Hit!')
                unite_1.health -= 20
        unite_1.health -= unite_2.attack / 10
        print('\nUnite 1:')
        print(unite_1.health)
        if unite_1.health == 0.0:
            break
if unite_1.health <= 0:
    print('\nUnite 2 win!')
elif unite_2.health <= 0:
    print('\nUnite 1 win!')