class flashcard:
    def __init__(self, word , meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return f"{self.word} means {self.meaning}"
flash = []
print ("welcome to flashcard app")
while True:
    word = input("enter a word: ")
    meaning = input("enter the meaning: ")
    flash.append(flashcard(word, meaning))
    cont = input("do you want to add another flashcard? (yes/no): ")
    if cont.lower() != "yes":
        break
print("\nYour flashcards:")
for card in flash:
    print(card)