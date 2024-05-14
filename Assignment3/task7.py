'''
task-7. Write a Python program to read a file line by line store it into a variable.
'''

file = open("task7.txt","w")
file.write("This is line 1\n")
file.write("This is line 2\n")
file.write("This is line 3\n")
file.write("This is line 4\n")
file.write("This is line 5\n")
file.close()
print("****************************************************")

n = ""

with open("task7.txt", "r") as file:
    for i in file:
        n += i

print("Print data from variable")
print("****************************************************\n")
print(n)
