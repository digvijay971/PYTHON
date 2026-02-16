a = int(input("unit de varna goli marunga : "))
if (a < 50):
    x=25+(a*2)
elif (a < 100):
    x =35+130+((a - 50)*3)
elif (a < 200):
    x = 45+130+162+(( a - 100)*5)
else:
    x = 130+162+526+((a - 200)*8)
print("li ght ki bill de : ", x)