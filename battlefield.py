
from robot import Robot
from dinosaur import Dinosaur
from weapon import w_one # added weapon nanme to display_welcome

dino_one = Dinosaur('Milo')
robo_one = Robot('C3P0')
class Battlefield:
    def __init__(self): 
        print()
        print(f'Welcome! Today we have {dino_one.name} battling {robo_one.name}! Who will win? Let\'s find out:') 
    
   
    def display_welcome(self):
        print(f'{robo_one.name}\'s weapon will be: {w_one.name} ')
    
    
    def battle_phase(self):
        while (dino_one.health > 0) and (robo_one.health > 0):
            dino_one.attack(robo_one)
            if (robo_one.health <= 0) and (dino_one.health > robo_one.health):
                print(f'{dino_one.name} defeated {robo_one.name}!')
                print(f'{dino_one.name} wins!')
                break
            elif (dino_one.health <= 0) and (robo_one.health > dino_one.health):
                print(f'{robo_one.name} defeated {dino_one.name}! ')
                print(f'{robo_one.name} wins!')
                break
            robo_one.attack(dino_one)
            if (robo_one.health <= 0) and (dino_one.health > robo_one.health):
                print(f'{dino_one.name} defeated{robo_one.name}!')
                print(f'{dino_one.name} wins!')
                break
            elif (dino_one.health <= 0) and (robo_one.health > dino_one.health):
                print(f'{robo_one.name} defeated {dino_one.name}! ')
                print(f'{robo_one.name} wins!')
                break
   
   
    def end_message(self):
        print('Thanks for watching! See you next time!')
    def run_game(self):
        self.__init__(1)
        self.display_welcome(1)
        self.battle_phase(1)
        self.end_message(1)

                  





    
    # def display_welcome(self):
    #     print('Welcome to the game! Who will go first?')
    # def battle_phase(self):
    #     print('Let the battle begin')

    #     dinosaur.dino_one.dino_attack()
    #     robot.robot_one.robo_attack()
    # def display_winner(self):
    #     pass


#going to go in battle phase?

    
