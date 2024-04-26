d = {124:"Akshay", 890:"Aarohi", 997:"Hamza", 545:"Rishil", 890:"Milin"}

print(d)

d[124] = "Uday"
print(d)

print(d[890])

#d.clear()
#print(d)

d1 = d.copy()

print(d1)

print(d.get(997))

print(d.items())
print(d.keys())
print(d.values())

print(d.pop(545))
print(d)

print(d.popitem())
print(d)

d2 = {345:"Shivam", 678:"Nirmal", 789:"Jay", 889:"Krishna"}
d.update(d2)
print(d)

print("\n")
print("Iterating Dictionary :")
for i in d:
    print(i, " : ",d[i])
