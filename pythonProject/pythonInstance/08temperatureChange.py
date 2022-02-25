# -*- coding: UTF-8 -*-
"""
    author:chl
    language:python
    requires:摄氏温度转华氏温度
"""
celsius = float(input("输入摄氏温度："))

fahrenheit = (celsius*1.8) + 32
print("摄氏温度{}转为华氏温度为{}".format(celsius,fahrenheit))


