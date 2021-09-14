class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14

print("Enter the value of radius")
r = int(input())
desiredCircle = Circle(r)
print("AREA OF DESIRED CIRCLE")
print(desiredCircle.area())
print("PERIMETER OF DESIRED CIRCLE")
print(desiredCircle.perimeter())
