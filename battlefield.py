
from robot import Robot
from dinosaur import Dinosaur
from weapon import w_one # added weapon nanme to display_welcome

class Battlefield:
    def __init__(self):
        self.dino_one = Dinosaur('Milo')
        self.robo_one = Robot('C3P0')
        print()
        print(f'Welcome to the arena! Today we have {self.dino_one.name} battling {self.robo_one.name}! Who will win? Let\'s find out:') 
    
   
    def display_welcome(self):
        print(f'{self.robo_one.name}\'s weapon will be: {w_one.name} ')
    
    
    def battle_phase(self):
        while (self.dino_one.health > 0) and (self.robo_one.health > 0):
            self.dino_one.attack(self.robo_one)
            if (self.robo_one.health <= 0) and (self.dino_one.health > self.robo_one.health):
                print(f'{self.dino_one.name} defeated {self.robo_one.name}!')
                print(f'{self.dino_one.name} wins!')
                break
            elif (self.dino_one.health <= 0) and (self.robo_one.health > self.dino_one.health):
                print(f'{self.robo_one.name} defeated {self.dino_one.name}! ')
                print(f'{self.robo_one.name} wins!')
                break
            self.robo_one.attack(self.dino_one)
            if (self.robo_one.health <= 0) and (self.dino_one.health > self.robo_one.health):
                print(f'{self.dino_one.name} defeated{self.robo_one.name}!')
                print(f'{self.dino_one.name} wins!')
                break
            elif (self.dino_one.health <= 0) and (self.robo_one.health > self.dino_one.health):
                print(f'{self.robo_one.name} defeated {self.dino_one.name}! ')
                print(f'{self.robo_one.name} wins!')
                break
   
   
    def end_message(self):
        print('Thanks for watching! See you next time!')
    def run_game(self):
        self.__init__()
        self.display_welcome()
        self.battle_phase()
        self.end_message()

                  




