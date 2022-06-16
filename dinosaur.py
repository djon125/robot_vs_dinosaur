import random


class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.attack_power = random.randint(1, 50) #attack_power if it doesn't work
        self.health = 100


    
    def dino_attack(self, robot): #dino attack robo
        robot.health -= self.attack_power