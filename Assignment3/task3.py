'''
Task-3. Write a Python program to append text to a file and display the text.
'''

file = open("task3.txt","w")
file.write("This is Task - 3...")
file.close()
print("File Written Successfully")
print("************************************************************")

file = open("task3.txt","r")
print(file.read())
file.close()
print("File reading complete... :)")
print("************************************************************")

file = open("task3.txt","a")
file.write("\nThis file is now appended.")
file.close()
print("File appended Successfully")
print("************************************************************")

file = open("task3.txt","r")
print(file.read())
file.close()
print("************************************************************")
