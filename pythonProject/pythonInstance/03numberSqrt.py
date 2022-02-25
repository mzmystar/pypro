# -*- coding: UTF-8 -*-
"""
    author:chl
    language:python
    requires:计算输入数字的平方根
"""

#如果不是数字将会报错 ValueError
num = float(input("输入一个数字："))
result = num ** 0.5
# import math;result = math.sqrt(num) #采用math模块内的sqrt()方法
# 该结果中只包含正整数，不包括负数
print("数字{}的平方根为{}".format(num,result))

#如果是负数、复数，采用 cmath （complex math）模块下的sqrt()方法
import cmath
cnum = float(input("输入一个数字："))
cresult = cmath.sqrt(cnum)
# cresult.real 实部 cresult.imag 虚部
print("数字{}的平方根为{}+{}j".format(cnum,cresult.real,cresult.imag))



