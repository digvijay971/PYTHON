import random 
a = True
b = str(random.randint(1, 10))
print("Welcome to the guessing game!")
print("I am thinking of a number between 1 and 10.")
while a:
    c = input("What is your guess? ")
    if c == b:
        print("Congratulations! You guessed the number!")
        a = False
    else:
        print("Sorry, that's not correct. Try again!")