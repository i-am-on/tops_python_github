'''
Write a Python program to replace last value of tuples in a list.
'''

l = [(10,20,30),(40,50,60),(70,80,90)]

a = 100

for i in range(len(l)):
    n = list(l[i])
    n[-1] = a
    l[i] = tuple(n)

print("After : ",l)
