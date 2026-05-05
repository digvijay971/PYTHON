import random
import string
a = 12
b = string.ascii_letters + string.digits + string.punctuation
c = ''.join(random.choice(b) for _ in range(a))
print("Welcome to the Random Password Game!")
print("Try to guess the generated password.")
print("You have 10 attempts.")
print("The password contains letters, numbers, and symbols.")
d = 10
e = 10
for d in range(1, e + 1):
    guess = input(f"Attempt {d}/{e}: ")
    if guess == c:
        print("Correct! You guessed the password.")
        break
    else:
        f = e - d
        print("Wrong password.")
        if f:
            print(f"Try again. Attempts remaining: {f}")
        else:
            print("No attempts left.")
            print(f"The password was: {c}")