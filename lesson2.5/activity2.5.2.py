a = int(input("enter a num now !"))
y = 1
for x in range(1,a + 1):
    for b in range(1,x + 1):
        print(y, end=" ")
        y = y + 1
    print()