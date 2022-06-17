import random
class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power



gun = Weapon('glock', random.randint(1, 20))
sword = Weapon('excalibur', random.randint(20, 30))
light_saber = Weapon('light saber', random.randint(30, 40))
bomb = Weapon('bombo', random.randint(50, 60))
gas = Weapon('gas', random.randint(15, 23))
crossbow = Weapon('arrow', random.randint(1, 15))

Weapons = [gun, sword, light_saber, bomb, gas, crossbow]
w_one = random.choice(Weapons)
