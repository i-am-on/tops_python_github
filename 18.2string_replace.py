s1 = input("Enter String1: ")
s2 = input("Enter String2: ")

c = s2[:2] + s1[2:] + ' ' + s1[:2] + s2[2:]

print("\n")
print("After swapping the first 2 characters of both strings:\n",c)
