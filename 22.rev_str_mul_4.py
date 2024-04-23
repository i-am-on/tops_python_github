s = input("Enter String: ")

if len(s) % 4 == 0:
    a = s[::-1]
else:
    a = s

print(a)
