
from weapon import w_one
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = w_one.attack_power #random choice weapon
    
    def attack(self, dinosaur): #robo attack dino- pass dino into it
        dinosaur.health -= self.active_weapon
        self.active_weapon = w_one.attack_power
        print(f'Dinosaur new health is: {dinosaur.health}')


    




