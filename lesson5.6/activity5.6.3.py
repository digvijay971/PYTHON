import random
class fruitquiz:
    def __init__(self):
        self.fruits = {"apple": "red", "banana": "yellow", "orange": "orange", "grape": "purple", "kiwi": "green"}
    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            answer = input(f"What color is a {fruit}? ")
            if answer.lower() == color:
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is {color}.")
            cont = input("Do you want to try another fruit? (yes/no): ")
            if cont.lower() != "yes":
                break
print("Welcome to the Fruit Quiz!")
quiz = fruitquiz()
quiz.quiz()