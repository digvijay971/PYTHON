def a(b):
    return b*1400
def c(d):
    if d == "manor":
        return 150
    elif d == "delhi":
        return 15000
    elif d == "mumbai":
        return 5000
    elif d == "america":
        return 10000000
def e(f):
    if f >= 7:
        return 40*f - 50
    elif f >= 3:
        return 40*f - 20
    else:
        return 40*f
b = int(input("Enter the number of days you want to stay: "))
d = input("Enter the city you want to stay in: ")
f = int(input("Enter the number of people you are travelling with: "))
print("The total cost of your trip is: ", a(b) + c(d) + e(f))