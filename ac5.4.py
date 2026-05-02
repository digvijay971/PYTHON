class stringreverse:
    def __init__(self, s):
        self.s = s

    def reverse(self):
        words = self.s.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
print(stringreverse("Hello World").reverse())