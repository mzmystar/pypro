# -*- coding: UTF-8 -*-
"""
    author:chl
    language:python
    requires:使用if...elif...else 语句判断正数、负数、零
"""
num = float(input("输入一个数字:"))

if num > 0:
    print("正数")
elif num == 0:
    print("零")
else:
    print("负数")

