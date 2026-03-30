def a(b):
    c = 0
    d = []
    for e in b:
        if len(e) > 1 and e[0] == e[-1]:
            c += 1
            d.append(e)
    print("both first and last characters are same: ", c)
    return d
e = a(["abc", "xyz", "aba", "1221"])
print("both first and last characters are same: ", e)