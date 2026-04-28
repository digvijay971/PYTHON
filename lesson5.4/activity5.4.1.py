class a:
    __privateVar = 70000000;
    def __privateMethod(self):
        print("This is a private method")
    def hello(self):
        print("Hello World this is my private variable: ", self.__privateVar)
obj = a()
obj.hello()
obj.__privateMethod