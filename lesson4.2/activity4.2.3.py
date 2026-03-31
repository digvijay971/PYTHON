a = (1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
b = 0
c = 0
for d in range(0,32):
    if(a[d]==0):
        c+=1
    else:
        b+=1
if(b>c):
    print("go play outside")
else:
    print("go play video games")    