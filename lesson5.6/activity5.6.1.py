class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if self.a < other.a:
            return "A is less than B"
        else:
            return "A is not less than B"
    def __eq__ (self, other):
        if self.a == other.a:
            return "A is equal to B"
        else:
            return "A is not equal to B"
a = A(5)
b = A(10)
print("passed values:", a.a, b.a)
print(a < b)
c = A(10)
d = A(10)
print("passed values:", c.a, d.a)
print(c == d)