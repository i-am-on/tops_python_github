'''
Write a Python program to map two lists into a dictionary
'''

keys = ['a', 'b', 'c']
values = [1, 2, 3]


d = {}


for i in range(min(len(keys), len(values))):
    
    d[keys[i]] = values[i]


print("After Maping Dictionary:", d)
