'''
Write a Python program to calculate the area of a trapezoid.
'''

b1 = float(input("Enter the length of the first base: "))
b2 = float(input("Enter the length of the second base: "))
h = float(input("Enter the height of the trapezoid: "))

area = 0.5 * (b1 + b2) * h

print("The area of the trapezoid is:", area)
