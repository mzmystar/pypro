# -*- coding: UTF-8 -*-
# 正则表达式re

import re

# re.match(pattern=,string=,flags=) 匹配成功返回一个匹配对象，否None;
# pattern re表达式 string:要匹配的字符串；flags:标志位，控制正则的匹配方式
str1 = 'natural creation'
print(re.match('n',str1).span())   #首位开始匹配
print(re.match('n',str1).group())   #首位开始匹配
print(re.match('.*[a-zA-Z]',str1))   #首位开始匹配

# re.search(pattern=,string=,flags=) 扫描整个字符串匹配

print(re.search('o',str1).span())
print(re.search('o',str1))

# re.sub(pattern=,repl=,string=,count=0,flags=0)
# repl：替换的字符或函数，count：替换的数量，默认0，表所有

print(re.sub('natural','artificial',str1))

# re.compile(pattern=,flags=) 编译正则表达式，生成一个pattern对象
# flags参数：
#     re.I  忽略大小写 ignore
#     re.L  表特殊字符集
#     re.M  多行模式
#     re.S  即为‘.’ 包括了换行符，('.'不包括)
#     re.U  表特殊字符集Unicode
#     re.X  忽略空格和‘#’后的注释，增强可读性

# re.findall() 在字符串中找到所有匹配的对象，返回类型为列表

print(re.findall('a',str1))



