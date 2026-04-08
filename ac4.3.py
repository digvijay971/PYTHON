# Program to check the frequency of a value in a dictionary

def check_value_frequency(a,b):
    c = 0
    for d in a:
        if a[d] == b:
            c += 1
    return c
e = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 1
}
f= 1
g = check_value_frequency(e, f)
print(f"The value {f} appears {g} times in the dictionary.")
