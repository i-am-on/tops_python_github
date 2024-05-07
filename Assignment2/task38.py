'''
Write a Python program to check multiple keys exists in a dictionary
'''

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


keys = ['d', 'c','a']

a=True

for i in keys:
    if i not in d:
        print("One or more keys do not exist in the dictionary.")
        a = False
        break
else:
    print("All keys exist in the dictionary.")
