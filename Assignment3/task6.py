'''
task-6.Write a Python program to read a file line by line
       and store it into a list
'''

file = open("task6","w")
file.write("This is line 1\n")
file.write("This is line 2\n")
file.write("This is line 3\n")
file.write("This is line 4\n")
file.write("This is line 5\n")
file.close()
print("****************************************************")


f_l = []

with open("task6", "r") as file:
    for i in file:
        f_l.append(i.strip())

print(f_l)
