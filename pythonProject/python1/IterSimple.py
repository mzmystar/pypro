# encoding : utf-8

# 迭代器，基本方法：next(),iter()
class IterSimple:
    def __iter__(self):
        self.it=1
        return self
    def __next__(self):
        nt=self.it
        self.it += 1
        return nt

itersimple = IterSimple()
num = iter(itersimple)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
