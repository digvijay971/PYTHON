a = float(input("total bill amount: "))
b = float(input("amount paid: "))
x = a - b
if x > 0:
    print("amount due:", x)
elif x == 0:
    print("no amount due")
else:
    print("change to be returned:", -x)