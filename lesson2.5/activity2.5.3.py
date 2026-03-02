a = int(input("enter a num now !"))
for x in range(1,a + 1):
    print(" " * (a - x) + "!" * x)
for x in range(a - 1,0,-1):
    print(" " * (a - x) + "!" * x)