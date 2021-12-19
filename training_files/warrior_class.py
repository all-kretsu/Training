# its a training file
# creating warrior class
import random


player_attack = random.randint(0,1)

class Warrior():
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health

    def unite_damage(self):
        if attack:
            health -= attack / 10


unite_1 = Warrior(100, 100)

unite_2 = Warrior(100, 100)

if player_attack == 0:
    unite_1.unite_damage()
    print(f'unite_2 health = {unite_2.health}')
elif player_attack == 1:
    unite_2.unite_damage()
    print(f'unite_1 health = {unite_1.health}')
else:
    pass
