'''
How can you pick a random item from a list or tuple?
'''

import random

my_list = [1, 2, 3, 4, 5]
random_item = random.choice(my_list)
print("Random item from the list:", random_item)

my_tuple = ('apple', 'banana', 'orange', 'grape')
random_item = random.choice(my_tuple)
print("Random item from the tuple:", random_item)
