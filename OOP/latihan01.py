# Build simple pong game









# Make OOP Heroes in Python
from itertools import count


class Hero:
    count=0
    def __init__(self, name, health, attackPower, armor):
        # instance variable
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armor
        count += 1
    def attack(self, enemy):
        enemy.health -= self.attackPower
        print(f'{self.name} menyerang {enemy.name}')
        print(f'{enemy.name} mendapatkan damage {self.attackPower}')
        print(f'{enemy.name} memiliki health {enemy.health}')
    def defense(self, enemy):
        self.health += self.attackPower
        print(f'{self.name} melakukan defense')
        print(f'{self.name} mendapatkan heal {self.attackPower}')
        print(f'{self.name} memiliki health {self.health}')
    def showHealth(self):
        print(f'{self.name} memiliki health {self.health}')
    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False

hero1 = Hero('sniper', 100, 10, 5)
print(hero1.__dict__)