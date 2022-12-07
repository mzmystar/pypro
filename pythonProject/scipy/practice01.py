# -*- coding: UTF-8 -*-
# import os
# for i in os.environ.keys():
#     print("{}:  {}".format(i,os.environ[i]))
print(chr(97))
print(ord('a'))

print(1 == 1 or 2 == 3) # type  boolean

def fun1():
    a = 1
    b = 2
    fun2(a,b) #
    print(a, b)
def fun2(a,b): # 局部变量
    a +=10
    b +=20
    print(a,b)
fun1()
