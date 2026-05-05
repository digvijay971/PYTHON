class vehicle:
    class bus:
        def __init__(self,km,price):
            self.km=km
            self.price=price
        def display(self):
            print("km=",self.km)
            print("price=",self.price)
v=vehicle()
b=v.bus(100,50000)  
b.display()