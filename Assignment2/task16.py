'''
Write a Python program to check whether a list contains a sub list
'''

l = [1,2,3,4,5,6,7,8]

l1 = [3,4,5]

a=False
for i in range(len(l) - len(l1)+1):
    if l[i:i+len(l1)] == l1:
        a = True
        break

if a:
    print("list has sublist")
else:
    print("list has no sublist")
