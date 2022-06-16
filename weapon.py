import random
class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power



gun = Weapon('glock', 20)
sword = Weapon('excalibur', 30)
light_saber = Weapon('light saber', 40)
bomb = Weapon('bombo', 50)
gas = Weapon('gas', 23)
crossbow = Weapon('arrow', 44)

Weapons = [gun, sword, light_saber, bomb, gas, crossbow]
w_one = random.choice(Weapons)
print(w_one.name)