# -*- coding: UTF-8 -*-
def fun(val,list=[]):
    list.append(val)
    return list
l1 = fun(10)
l2 = fun(123,[])
l3 = fun("a")
print(l1)
print(l2)
print(l3)

import logging,sys

"""
logging.debug(msg,*args,exc_info,stack_info,stacklevl,**kwargs)
在此记录器上记录debug级别的消息
msg 消息格式字符串
args 用于字符串格式化操作合并到msg的参数
    未提供args时，不会对msg执行 % 格式化操作
kwargs 中会检查四个关键字参数：exc_info、stack_info、stacklevel、extra
"""


Format = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(format=Format)
d = {'clientip':'192.168.0.1','user':'fbloggs'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem %s','connection reset',extra=d)
# 求取上升区间的总和
def maxProfit(list):
    if len(list)==0:
        return 0
    maxprofit=0
    for i in range(len(list)-1):
        res = list[i+1]-list[i]
        if res>0:
            maxprofit += res
    return maxprofit
list = [3,2,4,6,7,5,1]
maxprofit=maxProfit(list)
print("对于"+str(list)+"可获取的最大利润为："+str(maxprofit))
