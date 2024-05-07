'''
Write a Python program to select an item randomly from a list.
'''

import random

l = [i for i in range(1,11)]

random_list = random.choice(l)

print("Original List : ",l)
print("Random item from the list is : ",random_list)
