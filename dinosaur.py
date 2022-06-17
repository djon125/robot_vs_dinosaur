import random


class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.attack_power = random.randint(1, 50) #attack power random
        self.health = 100


    
    def attack(self, robot): #dino attack robo- passing in robot
        robot.health -= self.attack_power
        self.attack_power = random.randint(1, 50)
        print(f'Robot new health is: {robot.health}')