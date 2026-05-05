from abc import ABC, abstractmethod
class abclass(ABC):
    def print (self,x):
        print("The value of x is:",x)
    @abstractmethod
    def task(self):
        print("This is an abstract method")
class test(abclass):
    def task(self):
        print("This is the implementation of the abstract method")
t=test()
t.print(10)
t.task()