l = ["Elephant", "Donkey", "Monkey", "Seal", "Lion", "Dog"] 

max_length = 0
for i in l:
    if len(i)>max_length:
        max_length = len(i)

print("Longest word's length from the list is : ", max_length)
