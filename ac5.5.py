def int_to_roman(num):
    if not isinstance(num, int) or num <= 0 or num >= 4000:
        raise ValueError("Input must be an integer from 1 to 3999")

    roman_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = []
    for value, symbol in roman_map:
        count = num // value
        if count:
            result.append(symbol * count)
            num -= value * count
    return "".join(result)


if __name__ == "__main__":
    try:
        number = int(input("Enter an integer (1-3999): "))
        print(f"Roman numeral: {int_to_roman(number)}")
    except ValueError as error:
        print("Error:", error)
