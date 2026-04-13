a = [1,2,3]
b = [4,5,6]
c = map(lambda x,y: x+y, a, b)
print("The result of adding the two lists is:")
print(list(c))
d = [1,2,3,4,5]
def square(x):
    return x**2
e = list(map(square, d))
print("The result of squaring the elements of the list is:")
print(e)