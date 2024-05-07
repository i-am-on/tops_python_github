'''
Write a Python program to create a dictionary from a string.

Note: Track the count of the letters from the string.

Sample string: 'w3resource'
'''


string = 'w3resource'

count = {}

for i in string:
   if i in count:
        count[i] += 1
   else:
        count[i] = 1

print(count)
