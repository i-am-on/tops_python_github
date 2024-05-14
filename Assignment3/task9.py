'''
task-9. Write a Python program to count the number of lines in a text file. 
'''

file = open("task9.txt","w")
file.write("This is file write operation using python.\n")
file.write("This is line 1\n")
file.write("This is line 2\n")
file.write("This is line 3\n")
file.write("This is line 4\n")
file.write("This is line 5\n")
file.close()
print("File Written Successfully")
print("************************************************************")


line_count = 0

with open("task9.txt", "r") as file:
    for i in file:
        line_count += 1

print("Number of lines in the file is :", line_count)
