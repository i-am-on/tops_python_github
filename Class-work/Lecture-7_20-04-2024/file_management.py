file = open("tops1.txt","w")
file.write("This is file write operation using python.")
file.close()
print("File Written Successfully")
print("************************************************************")

file = open("tops1.txt","r")
print(file.read())
file.close()
print("************************************************************")

file = open("tops1.txt","a")
file.write("\nThis file is now appended.")
file.close()
print("File appended Successfully")
print("************************************************************")

file = open("tops1.txt","r")
print(file.read())
file.close()
print("************************************************************")


file = open("tops2.txt","w+")
file.write("This is w+ mode using python.")
print("Current File Position : ",file.tell())
file.seek(0)
print("File Content : ",file.read())
file.close()
print("-------------------------------------------------------------")





