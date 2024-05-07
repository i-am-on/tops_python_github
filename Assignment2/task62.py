'''
Write a Python program to calculate surface volume and area of a cylinder.
'''

pi=3.14

r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))

area = 2 * pi * r * (r + h)

volume = pi * r**2 * h

print("The surface area of the cylinder is:", area)
print("The volume of the cylinder is:", volume)
