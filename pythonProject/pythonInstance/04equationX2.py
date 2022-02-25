# -*- coding: UTF-8 -*-
"""
    author:chl
    language:python
    requires:通过用户输入数字，计算二次方程
    ax**2+bx+c=0
    x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
"""
import cmath
numa = float(input("输入a:"))
numb = float(input("输入b:"))
numc = float(input("输入c:"))

numd = numb**2 - 4 * numa * numc

result1 = (-numb + cmath.sqrt(numd))/(2*numa)
result2 = (-numb - cmath.sqrt(numd))/(2*numa)

print("方程解为{}和{}".format(result1,result2))
