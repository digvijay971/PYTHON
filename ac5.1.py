class Dog:
     species = "Canis familiaris"
     def __init__(self, name, breed):
        self.name = name
        self.breed = breed
     def display_details(self):
        """Display the details of the dog"""
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
        print("-" * 40)
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")
print("DOG DETAILS")
print("=" * 40)
print("\nDog 1:")
dog1.display_details()
print("Dog 2:")
dog2.display_details()