'''
Write a Python program to combine two dictionary adding values for
common keys.
'''

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200,'d':400}

d3={}

for i in d1:
    d3[i] = d1[i]
    if i in d2:
        d3[i] += d2[i]

for i in d2:
    if i not in d3:
        d3[i] = d2[i]

print("Combined Dictionary:", d3)
