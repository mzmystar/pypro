# -*- coding: UTF-8 -*-
"""
    author:chl
    language:python
    requires:求圆的面积
    S = PI*r**2
"""
import math
r = float(input("请给出圆的半径："))

S = math.pi*r**2

print("半径为{}的圆的面积为{}".format(r,S))


