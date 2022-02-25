import os
import os.path

oslist = dir(os) #获取os 内可调用的所有方法
print(oslist)
f1 = 'fileOperate/picklefile.txt'
print(os.path.dirname(f1))  #获取所选文件所在的目录名
print(os.getcwd())          #获取当前工作目录
print(os.path.basename(f1)) #获取所选文件的文件名
print(os.path.abspath(f1))  #获取文件的绝对路径
print(os.path.split(f1))
