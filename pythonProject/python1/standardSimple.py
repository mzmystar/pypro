
# 操作系统接口 os
import os
# 获取当前目录
print(os.getcwd())
#执行系统命令
os.system('echo date')

#管理日常的文件和目录管理任务 shutil
import shutil
shutil.copyfile('p1.py','p2.py')    #复制文件

#从目录通配符搜索中生成文件列表 glob模块内的glob()函数
import glob
filelist = glob.glob('*.py')
print(filelist)

# 调用命令行参数 。其已链表的形式存储于sys模块的argv变量
import sys
print(sys.argv) #可获取输入的参数

#正则表达式 字符串正则匹配
import re
print(re.findall('a[a-z]*','apple banana orange'))
# 数学模块,math 可调用诸多数学模块
import math
print(math.sin(math.pi/2))
# 随机数 random
import random
print(random.choice(['A','B','C','D']))

# 访问互联网 urllib
from urllib.request import urlopen
for line in urlopen('http://baidu.com'):
    line = line.decode('utf-8')
    if 'url' in line:
        print(re.findall('[a-zA-Z0-9]*',line))
    else:
        print(line)

# 日期和时间 datetime
from datetime import date
import time
td = date.today()
print(td)
tm = time.localtime()
print(tm)

# 压缩和打包 zlib\gzip\bz2\zipfile\tarfile
import zlib     #压缩
s = b"Don't forget, a person's greatest emotional need is to feel appreciated."
print(len(s))
zs = zlib.compress(s)
print(len(zs))
print(zlib.decompress(zs))

# 性能度量 timeit模块下的Timer
from timeit import Timer
print(Timer('n=a;a=b;b=n','a=3;b=4').timeit())
print(Timer('a,b=b,a','a=3;b=4').timeit())

#测试模块 doctest() 利用内嵌的文档字符串进行测试
import doctest
def average(values):
    """
    print(average([30,60,90]))
    60
    :param values:[30,60,90]
    :return:average(values)
    """
    return sum(values)/len(values)
print(doctest.testmod())





