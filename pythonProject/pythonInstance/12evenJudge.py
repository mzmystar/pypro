# -*- coding: UTF-8 -*-
"""
    author:chl
    language:python
    requires:判断奇数偶数
    奇数：odd
    偶数：even
    source:www.runoob.com
"""
def evenJudge(num):
    try:
        int(num)
    except (ValueError,TypeError):
        pass

    if num % 2 == 0:
        print("{}是偶数".format(num))
    else:
        print("{}是奇数".format(num))
evenJudge(9)
evenJudge(2e2)