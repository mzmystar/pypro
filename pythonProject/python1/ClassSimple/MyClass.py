
class MyClass():
    chinesename = 'zxc'     #公有属性
    _sex = '男'            #受保护的属性
    __ename = 'Stephen zhou'  #私有属性 无法在类外进行访问
    # 初始化构造函数  self 类的实例
    def __init__(self):
        self.chinesename = '周星驰'
    #普通函数
    def name(self):
        print('中文名：{}\n性别:{}\n英文名:{}'.format(self.chinesename,self._sex,self.__ename))
    # 私有方法只能在类的内部调用
    def __like(self):
        print("私有方法")

    def __call__(self, *args, **kwargs):
        self.__like()

if __name__ == "__main__":
    myClass = MyClass()
    print(myClass.chinesename)
    print(myClass._sex)
    #print(myClass.__ename) #类的私有属性无法在类型进行访问
    #myClass.__like()       #类的私有方法无法在类型进行访问
    myClass.name()
    myClass.__call__()