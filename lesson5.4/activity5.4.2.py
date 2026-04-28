class computer:
    def __init__(self):
        self.maxprice = 100000000
    def sell(self):
        print(f"Maximum Price: {self.maxprice}")
    def setMaxPrice(self, price):
        self.maxprice = price
c = computer()
c.sell()
c.setMaxPrice(70000000)
c.sell()