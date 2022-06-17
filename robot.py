
from weapon import w_one
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = w_one.attack_power #random choice weapon
    
    def attack(self, dinosaur): #robo attack dino- pass dino into method
        dinosaur.health -= self.active_weapon
        print(f'{self.name} attacked {dinosaur.name} with {w_one.name}! {dinosaur.name}\'s new health is: {dinosaur.health}')


    




