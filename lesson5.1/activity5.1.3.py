class a:
    b = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
c = a("blu", 15)
d = a("woo", 20)
print("Name of c is {} ".format(c.name))
print("Age of c is {} ".format(c.age))
print("Name of d is {} ".format(d.name))
print("Age of d is {} ".format(d.age))