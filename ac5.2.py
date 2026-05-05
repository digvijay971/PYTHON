a = int(input("Enter a radius: "))
class circle:
    pi = 3.14  
    def __init__(self, a):
        self.radius = a  
    def area(self):
        return circle.pi * (self.radius ** 2)
    def circumference(self):
        return 2 * circle.pi * self.radius
my_circle = circle(a)
print(f"Area of the circle: {my_circle.area()}")
print(f"Circumference of the circle: {my_circle.circumference()}")