# its a training file
import random


# creating warrior class
class Warrior():
    def __init__(self, turn, attack=100, health=100):
        self.attack = attack
        self.health = health
        self.turn = turn


# create example class
unite_1 = Warrior(0)
unite_2 = Warrior(1)

# 
while True:
    player_attack = random.randint(0,1)
    if player_attack == unite_1.turn:
            unite_2.health -= unite_1.attack / 10
            print('\nUnite 2:\n')
            print(unite_2.__dict__)
            if unite_2.health == 0.0:
                break
    elif player_attack == unite_2.turn:
            unite_1.health -= unite_2.attack / 10
            print('\nUnite 1:\n')
            print(unite_1.__dict__)
            if unite_1.health == 0.0:
                break
    else:
        pass
print(('Unite 1 win!') if unite_1.health > 0 
        else print('\nUnite 2 win!'))