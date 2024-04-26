#Function with No Argument & No Return Value.

def printLine():
    print("*"*60)

printLine()
print("Welcome To User Defined Function Using Python.")
printLine()


#Function No Argument & No Return Value.

def sum(a,b):
    print("Sum : ",a+b)

printLine()
x=int(input("Enter Value : "))
y=int(input("Enter Value : "))
sum(x,y)
printLine()


#Function With Argument & Return Value.

def sub(a,b):
    return a-b

printLine()
x=int(input("Enter Value : "))
y=int(input("Enter Value : "))
#ans  = sub(x,y)
print("Substraction : ", sub(x,y))
printLine()








