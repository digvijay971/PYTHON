age_input = input("Enter your age: ").strip()

if not age_input:
    print("Error: no age entered.")
else:
    if not age_input.isdigit():
        print("Error: age must be a positive integer.")
    else:
        age = int(age_input)
        if age < 0 or age > 120:
            print("Error: age must be a positive integer between 0 and 120.")
        else:
            if age % 2 == 0:
                print("Your age is even.")
            else:
                print("Your age is odd.")