'''
Write a Python function that takes two lists and returns true if they have 
at least one common member.
'''

l1 = [1,2,3]
l2 = [3,4,5]

if any(i in l1 for i in l2):

    print("List has at least 1 same value")

else:

    print("List has no same value")
