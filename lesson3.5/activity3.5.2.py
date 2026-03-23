import random
while True:
   a = input("choose (rock , paper" " or scissors) : ")
   b = random.choice(["rock", "paper", "scissors"])
   if a == b:
      print("It's a tie!")
   elif (a == "rock" and b == "scissors") or (a == "paper" and b == "rock") or (a == "scissors" and b == "paper"):
      print("You win!")
   else:
      print("You lose!")