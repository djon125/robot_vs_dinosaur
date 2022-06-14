
from dinosaur import dino_one
from weapon import light_saber

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = light_saber #hard coding in light saber
    
    def robo_attack(self, dino_hit):
        dino_hit = dino_one.health - robot_one.active_weapon.attack_power

    



        



robot_one = Robot('dion')

# print(dino_one.health)
# robot_one.robo_attack(1)
# print(dino_one.health)
# print(dino_one.health)
# robot_one.robo_attack(1)
# print(dino_one.health)