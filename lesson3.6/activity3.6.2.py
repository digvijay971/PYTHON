from datetime import date , time , datetime
import random
a = date(2020, 5, 17)
b = date(2021, 6, 18)
c = a + (b - a) * random.random()
print(c)