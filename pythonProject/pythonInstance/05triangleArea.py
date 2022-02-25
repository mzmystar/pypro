# -*- coding: UTF-8 -*-
"""
    author:chl
    language:python
    requires:计算三角形面积
    S = 1/2hl  底乘高除以2
    海伦公式：S = sqrt(p*(p-a)*(p-b)*(p-c))  p=(a+b+c)/2
"""
side1 = float(input("三角形第一条边长："))
side2 = float(input("三角形第二条边长："))
side3 = float(input("三角形第三条边长："))
# 半周长
circle = (side1+side3+side2)/2
# 海伦公式
S = (circle*(circle-side1)*(circle-side2)*(circle-side3))**0.5
print("三角形面积为：{}".format(S))
