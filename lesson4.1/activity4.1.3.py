a = [4,8,5,6,10,3,2,9,1,7]
print("original list: ", a)
b = 0
for c in a:
    b += c
print("sum of all elements: ", b)
d = b/len(a)
print("average of all elements: ", d)
e = a.sort()
print("sorted list: ", a)