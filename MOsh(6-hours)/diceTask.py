import random
class Dice:

    def roll(self):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return [x, y]


dice = Dice()
luck = dice.roll()
print(luck)