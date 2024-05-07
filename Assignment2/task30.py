'''
Write a Python program to convert a list of tuples into a dictionary.
'''

t = [("a", 1), ("b", 2), ("c", 3)]


d = {}


for key, value in t:
    d[key] = value


print("Dictionary is : ", d)
