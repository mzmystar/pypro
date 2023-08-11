# -*- coding: UTF-8 -*-
import math
def fun(n):
    # log 以3为底 N的对数 log3 取整进位 导致log(243,3)精度问题
    res=math.log10(n)/math.log10(3)
    if res%1==0:
        return True
    else:
        return False
res=fun(243)
print(res)
