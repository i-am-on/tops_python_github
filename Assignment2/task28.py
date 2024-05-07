'''
Write a Python program to remove an empty tuple(s) from a list of tuples
'''

l_t = [(1,2,3),(),(4,5,6),(),(),(8,2,7),(),(100,57,365)]

for i in (l_t):
    if not i:
        l_t.remove(i)

print(l_t)
