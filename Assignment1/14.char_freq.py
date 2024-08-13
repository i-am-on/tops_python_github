s = input("Enter a string: ")
count = 0

for i in range(0,len(s)):
    if (s[i]!=" "):
        count += 1

print("Total Number of Char in string : " + str(count))
