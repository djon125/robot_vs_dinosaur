# from robot import robot_one
import robot

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100


    
    def dino_attack(self): #dino attack robo
        print(f'Robot\'s health is: {robot.robot_one.health}')
        robot.robot_one.health = robot.robot_one.health -  dino_one.attack_power
        print(f'Robot\'s health is: {robot.robot_one.health}')


        
dino_one = Dinosaur('dino_one', 20)   
