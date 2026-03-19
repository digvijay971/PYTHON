a = False
while not a:
    try:
        x = int(input("Enter a number: "))
        while x%2 == 0:
          print("bye")
        a = True
    except ValueError:
        print("you are very very dumb") 