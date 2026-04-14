import random
a = random.randint(1, 10)
b = 3
print("welcome to the guessing game! you have 3 chances to guess the number between 1 and 10")
while b > 0:
    guess = int(input("enter your guess: "))
    if guess == a:
        print("congratulations! you guessed the number!")
        break
    elif guess < a:
        print("too low! try again.")
    else:
        print("too high! try again.")
    b -= 1
else:
    print("sorry, you ran out of chances. the number was " + str(a))