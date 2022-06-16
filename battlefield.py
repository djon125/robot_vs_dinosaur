#from robot import robot_one
#from dinosaur import dino_one
import dinosaur
import robot
#import weapon #not accessed


class Battlefield:
    def __init__(self):
        print('this is cool')
    def run_game(self):
        print('leggo')
        while (dinosaur.dino_one.health > 0) and (robot.robot_one.health > 0):
            dinosaur.dino_one.dino_attack()
            robot.robot_one.robo_attack()
            if (dinosaur.dino_one.health > robot.robot_one.health < 0):
                print(f'Dinosaur: {dinosaur.dino_one.name} wins!')
            elif (dinosaur.dino_one.health < robot.robot_one.health < 0):
                print(f'Robot: {robot.robot_one.name} wins! ')
                  

           # if (dinosaur.dino_one.health < 0) or (robot.robot_one.health < 0):



    
    
    
    
    
    
    
    # def display_welcome(self):
    #     print('Welcome to the game! Who will go first?')
    # def battle_phase(self):
    #     print('Let the battle begin')

    #     dinosaur.dino_one.dino_attack()
    #     robot.robot_one.robo_attack()
    # def display_winner(self):
    #     pass


#going to go in battle phase?
#dinosaur.dino_one.dino_attack()
# robot.robot_one.robo_attack()
# robot.robot_one.robo_attack()
# dinosaur.dino_one.dino_attack()
# dinosaur.dino_one.dino_attack()
# dinosaur.dino_one.dino_attack()
# dinosaur.dino_one.dino_attack()






    
