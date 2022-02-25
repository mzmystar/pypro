# -*- coding: UTF-8 -*-
"""
    author:chl
    language:python
    requires:判断字符串是否为数字
    source:www.runoob.com
"""
def number_judge(num):
    try:
        float(num)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(num)
        return True
    except (ValueError,TypeError):
        pass
    return False
print(number_judge('23.32'))

