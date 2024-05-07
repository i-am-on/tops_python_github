'''
Write a Python function that takes a list and returns a new list with unique 
elements of the first list.
'''

l1 = [1, 2, 2, 3, 3, 4, 5, 5,100,99,25,36,36,100,1001,99,25,36,1001,100,36]
l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)


print("Original list : ", l1)
print("List with unique elements : ", l2)
