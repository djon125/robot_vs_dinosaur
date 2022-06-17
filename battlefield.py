
from robot import Robot
from dinosaur import Dinosaur

dino_one = Dinosaur('dino_one')
robo_one = Robot('robo_one')
class Battlefield:
    def __init__(self): 
        print('Let\'s start the battle!') 
    
    def display_welcome(self):
        print('start the game, display self')
    def battle_phase(self):
        while (dino_one.health > 0) and (robo_one.health > 0):
            dino_one.attack(robo_one)
            if (robo_one.health <= 0) and (dino_one.health > robo_one.health):
                print(f'Dinosaur: {dino_one.name} wins!')
                break
            elif (dino_one.health <= 0) and (robo_one.health > dino_one.health):
                print(f'Robot: {robo_one.name} wins! ')
                break
            robo_one.attack(dino_one)
            if (robo_one.health <= 0) and (dino_one.health > robo_one.health):
                print(f'Dinosaur: {dino_one.name} wins!')
                break
            elif (dino_one.health <= 0) and (robo_one.health > dino_one.health):
                print(f'Robot: {robo_one.name} wins! ')
                break
    def run_game(self):
        self.display_welcome(1)
        self.battle_phase(1)
        # while (dino_one.health > 0) and (robo_one.health > 0):
        #     dino_one.attack(robo_one)
        #     if (robo_one.health <= 0) and (dino_one.health > robo_one.health):
        #         print(f'Dinosaur: {dino_one.name} wins!')
        #     elif (dino_one.health <= 0) and (robo_one.health > dino_one.health):
        #         print(f'Robot: {robo_one.name} wins! ')
        #     robo_one.attack(dino_one)
        #     if (robo_one.health <= 0) and (dino_one.health > robo_one.health):
        #         print(f'Dinosaur: {dino_one.name} wins!')
        #     elif (dino_one.health <= 0) and (robo_one.health > dino_one.health):
        #         print(f'Robot: {robo_one.name} wins! ')
                  





    
    # def display_welcome(self):
    #     print('Welcome to the game! Who will go first?')
    # def battle_phase(self):
    #     print('Let the battle begin')

    #     dinosaur.dino_one.dino_attack()
    #     robot.robot_one.robo_attack()
    # def display_winner(self):
    #     pass


#going to go in battle phase?

    
