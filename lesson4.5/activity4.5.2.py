a = [1, 2, 3]
b = ['a', 'b', 'c']
c = list(zip(a, b))
print("The result of zipping the two lists is:")
print(c)
d = [10,20,30,40]
e = [100,200,300,400]
for x, y in zip(d, e[::-1]):
    print(x,y)
f = ['gold', 'silver', 'usd/inr']
g = [4740,74,93.5]
h = {f: g for f,
      g in zip(f, g)}
print("The result of creating a dictionary from the two lists is:")
print(h)