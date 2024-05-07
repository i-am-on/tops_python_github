'''
Write a Python program to find the highest 3 values in a dictionary.
'''

d = {'a': 10, 'b': 60, 'c': 100, 'd': 84, 'e': 15}

sorted_values = sorted(d.values(), reverse=True)
highest_3 = sorted_values[:3]

print("Highest 3 values in the dictionary:", highest_3)
