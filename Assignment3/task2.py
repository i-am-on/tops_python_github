'''
Task-2. Write a Python program to read an entire text file.
'''

file = open("task2.txt","w")
file.write("This is task2!!!")
file.close()
print("File Written Successfully!!!\n")

file = open("task2.txt", "r")
print(file.read())
file.close()
print("\nFile reading complete!")
