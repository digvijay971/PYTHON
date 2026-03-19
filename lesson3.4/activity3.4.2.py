try:
    a,b = eval(input("Enter two numbers: , separated by a comma: "))
    x = a/b
    print("The result of a/b is: ", x)
except ZeroDivisionError:
    print("You cannot divide by zero, you are very very dumb")
except SyntaxError:
    print("You did not enter the numbers in the correct format, you are pagal")
except:
    print("An error occurred")
else:
    print("The division was successful")
finally:
    print("This will always be executed")