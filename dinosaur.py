# from robot import robot_one
import robot
import random

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = random.randint(1, 50) #attack_power if it doesn't work
        self.health = 100


    
    def dino_attack(self): #dino attack robo
        if robot.robot_one.health > 0:
            print(f'Robot\'s health is: {robot.robot_one.health}')
            robot.robot_one.health = robot.robot_one.health -  dino_one.attack_power
            dino_one.attack_power = random.randint(1, 50)
            print(f'Robot\'s health is: {robot.robot_one.health}')
        else:
            print('Uhoh, robo loses!')


        
dino_one = Dinosaur('dino_one', 40)   
