
from robot import Robot
from dinosaur import Dinosaur

robo_one = Robot('robo_one')
dino_one =Dinosaur('dino_one')
class Battlefield:
    def __init__(self):
        print('this is cool')
    def run_game(self):
        print('leggo')
        while (dino_one.health > 0) and (robo_one.health > 0):
            dino_one.dino_attack()
            robo_one.robo_attack()
            if (dino_one.health > robo_one.health < 0):
                print(f'Dinosaur: {dino_one.name} wins!')
            elif (dino_one.health < robo_one.health < 0):
                print(f'Robot: {robo_one.name} wins! ')
                  

           if (dinosaur.dino_one.health < 0) or (robot.robot_one.health < 0):


# print(robo_one.health)
# dino_one.attack(robo_one)
# print(robo_one.health)
# dino_one.attack(robo_one)
# print(dino_one.health)
# robo_one.attack(dino_one)
# print(dino_one.health)
# robo_one.attack(dino_one)
# print(dino_one.health)
# robo_one.attack(dino_one)
    
    # def display_welcome(self):
    #     print('Welcome to the game! Who will go first?')
    # def battle_phase(self):
    #     print('Let the battle begin')

    #     dinosaur.dino_one.dino_attack()
    #     robot.robot_one.robo_attack()
    # def display_winner(self):
    #     pass


#going to go in battle phase?

    
