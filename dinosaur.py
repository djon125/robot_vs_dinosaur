from robot import robot_one
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100


    
    def dino_attack(self, robot_hit):
        self.robot_hit = robot_one.health -  dino_one.attack_power

    # def dino_attack(self, hit_robot):
    #     self.hit_robot = True
        
dino_one = Dinosaur('dino_one', 20)   

# print(robot_one.health)

# dino_one.dino_attack(1)

# print(robot_one.health)

# dino_one.dino_attack(1)
# print(robot_one.health)