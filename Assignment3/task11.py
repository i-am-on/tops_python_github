'''
task-11. Write a Python program to write a list to a file. 
'''

l = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5"]

with open('task11.txt', 'w') as file:
    
    for i in l:
        file.write(str(i) + '\n')

print("List data written in file complete!!!")
