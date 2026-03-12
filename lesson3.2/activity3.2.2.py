def a(n):
    return n*n*n
def b(n):
    if n %3 ==0:
        return a(n)
    else:
        return False
print(b(9))
print(b(4))