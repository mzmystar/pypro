#encoding:utf-8

f1 = open('fileOperate/.poem.txt','w+')
# f1.write('''
# 渭城朝雨浥轻尘
# 客舍青青柳色新
# 劝君更尽一杯酒
# 西出阳关无故人
# ''')
# f2 = open('copyPoem.txt','w+')
f2 = open('fileOperate/copyPoem.txt', 'r')

file1 = f2.readlines() #类型为列表类型
print(type(file1))
# f2.seek(offset,from_what) 偏移量 from_what:0、开头；1、当前位置；2、末尾
print(len(file1))
for i in range(len(file1)):
    if i % 2 == 0 :
        f1.write('\n')
    else:
        try:
            s = (file1[i] + file1[i+1]).replace('\n','')#file1[i+1]可能会下标越界
            f1.write(s)
            print(f1.tell())#返回文件光标当前所处位置，从文件开头算起的字节数
        except IndexError:
            print('IndexError')
f2.close()
f1.close()
