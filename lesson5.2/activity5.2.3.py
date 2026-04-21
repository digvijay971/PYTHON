class PairFinder:
    def __init__(self, numbers):
        self.numbers = numbers
    def find_pairs_by_sum(self, target_sum):
        pairs = []
        for i in range(len(self.numbers)):
            for j in range(i + 1, len(self.numbers)):
                if self.numbers[i] + self.numbers[j] == target_sum:
                    pairs.append((i, j, self.numbers[i], self.numbers[j]))
        return pairs
if __name__ == "__main__":
    tuple_numbers = (10, 20, 30, 40, 50, 60, 70)
    finder = PairFinder(tuple_numbers)
    try:
        target_sum = int(input("Enter the sum you want to find: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        exit()
    result = finder.find_pairs_by_sum(target_sum)
    print(f"\nTuple: {tuple_numbers}")
    print(f"Target Sum: {target_sum}\n")
    if result:
        print(f"Pairs that add up to {target_sum}:")
        for idx1, idx2, num1, num2 in result:
            print(f"  Position {idx1} and {idx2}: {num1} + {num2} = {target_sum}")
    else:
        print(f"No pairs found that add up to {target_sum}")
