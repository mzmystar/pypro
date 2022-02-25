# -*- coding: UTF-8 -*-

class MyClass:
    # 构造方法   初始化
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def speak(self):
        print("name:{}\nage:{}\naddress:{}\n".format(self.name, self.age, self.address))

    def fun(n):
        try:
            if n >= 1:
                for i in range(n):
                    print(i)
            else:
                print(n)
        except  IndexError:
            pass

# 类的继承  单继承
class HeClass(MyClass):
    def __init__(self,age,address,name,favor):
        MyClass.__init__(self, age, address,name)
        self.favor = favor
    # 方法重载
    def speak(self):
        print("name:{}\nage:{}\naddress:{}\nfavor:{}".format(self.name, self.age, self.address,self.favor))


if __name__ == '__main__':
    # 类的实例化
    myclass = MyClass('Tom', 23, 'America')
    heclass = HeClass('ken',23,'A','sleep')
    # myclass.fun()
    myclass.speak()
    heclass.speak()


