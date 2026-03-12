def a(x):
    if x==0 or x==1:
        return 1
    else:
        return x*a(x-1)
print(a.__doc__)
print("the factorial of 0 is",a(0))
print("the factorial of 1 is",a(1))
print("the factorial of 2 is",a(2))
print("the factorial of 5 is",a(5))
print("the factorial of 10 is",a(10))