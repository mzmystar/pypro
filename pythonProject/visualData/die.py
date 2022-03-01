# -*- coding: UTF-8 -*-
from random import randint
class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    # 投掷骰子的动作
    def roll(self):
        return randint(1,self.num_sides)