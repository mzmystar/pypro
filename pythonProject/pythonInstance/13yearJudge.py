# -*- coding: UTF-8 -*-
"""
    author:chl
    language:python
    requires:对于给出的年份判断出是否是闰年
    闰年：整百年被四百整除；非整百年被四整除
    source:www.runoob.com
"""
def yearJudge(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                print("{}是闰年".format(year))
            else:
                print("{}不是闰年".format(year))
        else:
            print("{}是闰年".format(year))
    else:
        print("{}不是闰年".format(year))


# Python 内置 calendar 模块的isleap()方法可判断  leap year 闰年
import calendar
year = int(input("输入一个年份："))
print(calendar.isleap(year))

yearJudge(year)