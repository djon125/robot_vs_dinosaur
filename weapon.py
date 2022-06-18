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
crossbow = Weapon('crossbow', random.randint(1, 15))
throwing_star = ('throwing stars', random.randint(5, 15))
machine_gun = ('ak 47', random.randint(23, 33))

Weapons = [gun, sword, light_saber, bomb, gas, crossbow, throwing_star, machine_gun]

#random choice from weapon list
w_one = random.choice(Weapons)


