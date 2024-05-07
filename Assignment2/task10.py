'''
Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30.
'''

list = [i**2 for i in range(1, 31)]

ans = list[:5] + list[-5:]

print("First and last 5 elements squared between 1 and 30:",ans)
