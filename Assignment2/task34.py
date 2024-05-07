'''
Write a Python script to check if a given key already exists in a 
dictionary.
'''

d = {"a": 123, "b": 456, "c": 789, "d": 135, "e": 246, "f": 579}

f = "a"

if f in d:
    print("key is in dictionary")
else:
    print("Not in dictionary")
