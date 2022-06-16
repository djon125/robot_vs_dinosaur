
from weapon import w_one

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = w_one.attack_power #random choice weapon
    
    def attack(self, dinosaur): #robo attack dino
        dinosaur.health -= self.active_weapon

    




