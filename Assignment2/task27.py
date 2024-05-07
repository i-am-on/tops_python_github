'''
Write a Python program to find the repeated items of a tuple.
'''

t = (1,2,3,3,4,5,6,7,7,8,8,9,10,10)

empty_l = []

for i in t:
    if t.count(i)>1:
        if i not in empty_l:
            empty_l.append(i)

print("Repeated items of a tuple : ", empty_l)
