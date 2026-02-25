a = int(input("ggggggggiiiiiiiiivvvvvvvvvvvvvvvvvvvveeeeeeeeeeeeeeeeee             aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa             nnnnnnnnnnnnnnnnuuuuuuuuuuuummmmmmmmmmmmmmmmmmmbbbbbbbbbbbbbbbbeeeeeeeeeeeerrrrrrrrrrrrrr "))
b = str(a)
if len(b) >= 4 :
    x = len(b) // 2
    y = int(b[x - 1])
    z = int(b[x])
    print("the product of middle numbers are ",y * z)
else:
    print("get out")