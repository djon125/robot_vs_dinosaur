
# from dinosaur import dino_one
# from weapon import light_saber
import dinosaur
import weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = weapon.light_saber #hard coding in light saber
    
    def robo_attack(self): #robo attack dino
        print(f'Dino\'s health is: {dinosaur.dino_one.health}')
        dinosaur.dino_one.health = dinosaur.dino_one.health - robot_one.active_weapon.attack_power
        print(f'Dino\'s health is: {dinosaur.dino_one.health}')

    


        



robot_one = Robot('dion')

