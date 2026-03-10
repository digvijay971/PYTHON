def a(A,B):
    return A + B
def s(A,B):
    return A - B
def m(A,B):
    return A * B
def d(A,B):
    return A / B
print("what youwant to do")
print("a. add")
print("b. substract")
print("c. multiply")
print("d. divide")
b=input("(a/b/c/d)")
n_1= int(input("say"))
n_2= int(input("tell"))
if b =="a":
    print(n_1, "+", n_2, "=", a(n_1,n_2))
elif b =="b":
    print(n_1, "-", n_2, "=", s(n_1,n_2))
elif b =="c":
    print(n_1, "*", n_2, "=", m(n_1,n_2))
elif b =="d":
    print(n_1, "/", n_2, "=", d(n_1,n_2))
else:
    print("wrong input")