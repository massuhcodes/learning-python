from math import floor
from random import randint, seed

class Character:
    def __init__(self):
        self.strength = Character.roll_four_dice()
        self.dexterity = Character.roll_four_dice()
        self.constitution = Character.roll_four_dice()
        self.intelligence = Character.roll_four_dice()
        self.wisdom = Character.roll_four_dice()
        self.charisma = Character.roll_four_dice()
        self.hitpoints = 10 + modifier(self.constitution)
        
    def ability(self):
        # seed for difference output each execution
        seed(1)
        choice = {
            1:self.strength,
            2:self.dexterity,
            3:self.constitution,
            4:self.intelligence,
            5:self.wisdom,
            6:self.charisma
        }
        return choice[randint(1,6)]
    
    def roll_four_dice():
        seed(2)
        roll = [randint(1,6) for _ in range(4)]
        return sum(sorted(roll, reverse=True)[:3])

def modifier(constitution):
    return floor((constitution - 10) / 2)

