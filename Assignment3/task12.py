'''
task-12. Write a Python program to copy the contents of a file to another file.
'''
file = open("task12_1.txt","w")
file.write("Original File Content...!")
file.close()
print("File Written Successfully...")
print("*****************************")


with open("task12_1.txt", "r") as file1:
    a = file1.read()

with open("task12_2.txt", "w") as file2:
    file2.write(a)

print("Original file have been copied to the another file successfully!!")
