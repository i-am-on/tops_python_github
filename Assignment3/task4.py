'''
task-4. Write a Python program to read first n lines of a file.
'''

file = open("task4.txt","w")
'''
file.write("This is line 1.\n")
file.write("This is line 2.\n")
file.write("This is line 3.\n")
file.write("This is line 4.\n")
file.write("This is line 5.\n")
file.write("This is line 6.\n")
file.write("This is line 7.\n")
file.write("This is line 8.\n")
file.write("This is line 9.\n")
file.write("This is line 10.")
'''
file.close()
print("File Written Successfully")

#file_name = 'task4.txt'
n = 5

with open('task4.txt', 'r') as file:
    for _ in range(n):
        line = file.readline().strip()
        if not line:
            print("There is no line available to print")
            break
        print("\n",line)
