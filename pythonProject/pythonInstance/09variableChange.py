# -*- coding: UTF-8 -*-
"""
    author:chl
    language:python
    requires:变量交换
    变量：variable
    常量：constant
"""
v1 = input("变量1：")
v2 = input("变量2：")
# 变量交换
v1 ,v2 = v2,v1
print("交换后：\n变量1：{}\n变量2：{}".format(v1,v2))