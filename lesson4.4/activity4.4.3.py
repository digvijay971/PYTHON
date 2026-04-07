import array as arr
a = arr.array('i',[1,2,3,4,5,5,7,3,6,7,5,7,9,5,9,7,7,3,3,3,9,3])
print("Original:", str(a))
print("Count of 3:", a.count(3))
a.reverse()
print("Reversed:", str(a))