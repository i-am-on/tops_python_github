'''
task-5. Write a Python program to read last n lines of a file.
'''



file = open("task5.txt","w")
file.write("This is line1\n")
file.write("This is line2\n")
file.write("This is line3\n")
file.write("This is line4\n")
file.write("This is line5\n")
file.write("This is line6\n")
file.write("This is line7\n")
file.write("This is line8\n")
file.write("This is line9\n")
file.write("This is line10\n")
file.close()
print("File Written Successfully")
print("************************************************************")


f_name = 'task5.txt'
n = 5

with open("task5.txt", "r") as file:
    lines = file.readlines()
    last_n_lines = lines[-n:]

for i in last_n_lines:
    print(i.strip())
