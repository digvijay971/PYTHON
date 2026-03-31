def a(b):
    c = len(b) -1
    d = 0
    while(d<c):
        if(b[d]!=b[c]):
            return False
        d+=1
        c-=1
    return True
b =(1,2,3,3,2,1)
if(a(b)):
    print("palindrome")
else:
    print("not palindrome")