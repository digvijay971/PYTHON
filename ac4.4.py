a = input("Enter elements of the first set separated by spaces: ")
b = input("Enter elements of the second set separated by spaces: ")
c = set(a.split())
d = set(b.split())
e = c ^ d
print("Symmetric difference:", e)
