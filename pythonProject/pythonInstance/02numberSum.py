# -*- coding: UTF-8 -*-
"""
    author:chl
    require:输入两个数字，计算数字之和
"""
# 从输入窗口读取的数据类型为字符串类型
num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")
try:
    result = float(num1) + float(num2)
    print("数字{}与数字{}的和为{}".format(num1,num2,result))
except TypeError:
    pass


