
# import sys;x='python';sys.stdout.write(x+'\n');
# import keyword
# print(keyword.kwlist)
'''keyword 关键字
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async'(asynchronous), 'await', 'break',
'class', 'continue', 'def', 'del', 'elif', 'else',
'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

#
# #ord() 将一个字符转换成它的整数值
# #chr() 将一个整数转换成字符 character
# x='a';    a=97;
# print(ord(x));    print(chr(a))
#
def strSimple():
    print(dir(str))
    '''
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
    '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
    '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
    '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', 
    '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
    'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
    'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 
    'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 
    'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase','title','translate', 'upper', 'zfill']
    '''
    s='3'
    print(s.rjust(2))#右对齐
    print(s.ljust(2))#左对齐
    print(s.center(2).zfill(5))#零填充补位

def listSimple():
# list 列表（可变数据）：以超过字符长度的下标访问列表内的元素： 报越界错误，
# 已区间形式进行访问不会报错,左闭右开
    l1=[1,2,3,4];   print(l1[0:6]) #[1,2,3,4] 切片
    l1[0]=5;        print(l1) #[5,2,3,4] 修改数据
    print(l1[6:10]) #[]
    print(l1[-1:0:-1]) # 步长-1 [4,3,2]
    print(l1[-1::-1]) # 步长-1 [4,3,2,5]
    print(l1.index(4))# 3 查找列表内某元素所处位置，返回值为其下标，对于多个相同元素只返回最近的一个
    print(l1.count(2))# 1 统计列表内某元素的数据量
    print(l1.append(1))# 列表尾部追加元素，无返回值
    print(l1.insert(2,3))#指定下标2插入元素3，无返回值
    print(l1.pop())#1 返回所删除元素
    # print(l1.clear())#清空列表内元素，无返回值
    # print(l1.remove(2))#删除指定元素，无返回值；列表内无该元素，运行报错ValueError:x not in list
    print(l1.copy())#浅拷贝 复制元素给新对象，返回结果为原列表内元素，两者之间id不同，元素相同，互不影响
    l2 = l1.copy();l1.pop()
    print(id(l1),id(l2));print(l1,l2)
    print(l1.extend(l2))# l1拓展l2内元素，已追加的形式，无返回值
    #同时遍历两个列表，木桶效应，取最短
    d1 = [1,2,3,4]
    d2 = ['one','two','three']
    for i,j in zip(d1,d2):
        print(i,j)

def tupleSimple():
#tuple 元组（不可变数据）：数据不可改变
# 以超过字符长度的下标访问列表内的元素： 报越界错误，已区间形式进行访问不会报错
    t1=(1,2,3,4,);   print(t1[2:6])
    #元组内的数据不可变，无法进行修改
    #可用方法
    print(dir(tuple))
    '''元组关键字
    ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__','__dir__', '__doc__','__eq__',
    '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__','__gt__', '__hash__', '__init__', 
    '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
    '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__','count','index']
    '''

def dictSimple():
#dictionary 字典（可变数据）：通过键值对匹配，通过 键 访问 值
#键值对 ：键:不可变数据 即为num、string、tuple类型；在该字典内，唯一；
# keys():展示该字典内所有的键；
# values():展示该字典内所有的值；
    d1={'a':97,'b':98,'c':99};   print(d1['a'])
    print(d1.keys());   print(d1.values()) #分别获取字典内的键和值


def setSimple():
# set 集合 可变数据：元素不重复，唯一 ;不可进行切片操作
# 主要进行检测、判断、去重；集合运算:- | ^ &
    s1 = {1,2,3,4,5}; s2 = {2,4,6,8,0}
    print(s1-s2)    #集合1中去除存在于集合2中的元素
    print(s1|s2)    #取所有元素，自动去重排序（升序）
    print(s1^s2)    #去除共同元素
    print(s1&s2)    #取共同元素


'''chr(10),转字符为换行；十六进制： \x0a；  八进制：\012 同样为换行'''
print(chr(10))
print("123\x0a321\012321")

def randomSimple():
    import math,random
    '''对于round()函数，当小数点左侧为偶数时，若只有尾数>5时取上，否则舍弃
    round()函数：四舍六入五看齐，奇进偶不进。'''
    print(round(10.5),round(10.500000),round(10.500000001))
    print(round(11.55))
# listSimple()
# tupleSimple()
# strSimple()
import glob
# glob模块提供了一个glob()函数用于从目录通配符搜索中生成文件列表
l1 = glob.glob('*.py')
print(type(l1),l1)