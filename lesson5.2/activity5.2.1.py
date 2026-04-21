class a:
    def __init__(self):
        self.d = ""
    def b(self):
        self.d = input("Enter a string: ")
    def c(self):
        print("The string is: ", self.d.upper())
d = a()
d.b()
d.c()