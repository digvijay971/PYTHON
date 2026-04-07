a = {1,2,3}
print(a)
b = {1.0,"hi",(1,2,3)}
print(b)
c = {1,2,3,4,2,4,3,1}
print(c)
d = set([1,2,3,4,3,2])
print(d)
e = set([0,1,2,3,4,5])
print("original:",e)
e.pop()
print("after pop:",e)