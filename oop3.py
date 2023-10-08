class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
area = circle.calculate_area()
print("Area:", area)
print(circle)