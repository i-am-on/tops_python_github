import math

class Circle:
    def area(self,radius):
        return math.pi * radius * radius

    
    def perimeter(self,radius):
        return 2 * math.pi * radius


circle = Circle()

print("Area of Circle is: ",circle.area(5))
print("Perimeter of Circle is: ",circle.perimeter(5))
