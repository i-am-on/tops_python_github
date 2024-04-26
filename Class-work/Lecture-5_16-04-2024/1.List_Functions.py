l = [1,2,1.1,2.2,"tops",True,"Python",10,20,1,2]

#len fuction count the length of the List
#print(len(l))
print(l)
print("\n")

#append function add the given value at the end of the list
l.append(100)
print(l)
print("\n")

#clear function delete all the values from the list and make it empty
#l.clear()
#print(l)

'''
copy function copy all the values of one list to another list,
we need 2 variables for that one for original list
and another for copy the list
'''
l1=l.copy()
print(l1)
l1.append(200)
print(l1)
print(l)
print("\n")

'''
we can change the name of the list like shown below
and call it with another variable but if we change list
using another variable changes will apply to original list.
'''
l2=l
print(l2)
l2.append(300)
print(l2)
print(l)
print("\n")

'''
count function will count given value in a list
'''
print(l.count(1))
print("\n")

'''
extend function merge two list,
second list merge at the end of the first list
'''
l3 = [1000,2000]
l.extend(l3)
print(l)
print("\n")

#index function will show the index of given value
print(l.index(10))

#insert function will add any given value on specific given index,
#first parameter is index and second is value
l.insert(5,1010)
print(l)
print("\n")

'''
pop will remove the last element of the list,
if not given any specific index, if any index is given
it will remove the value from that index
'''
l.pop()
print(l)
print("\n")

l.pop(5)
print(l)
print("\n")

'''
remove function will remove the specific value from the list,
it will always remove the first value from the list,
it can remove only one value at a time
'''
l.remove(10)
print(l)
print("\n")

#It will reverse the whole list
l.reverse()
print(l)
