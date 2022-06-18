import random


class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.attack_power = random.randint(1, 50) #attack power random
        self.health = 100


    
    def attack(self, robot): #dino attack robo- passing robot into method
        robot.health -= self.attack_power
        self.attack_power = random.randint(1, 50)
        print(f'{self.name} attacked {robot.name} with his claws! {robot.name}\'s new health is: {robot.health}')