print("Start Code")

try:
    a = int(input("Enter value : "))
    b = int(input("Enter value : "))

    c=a/b
    print("Division : ",c)

except Exception as e:
    print("Exception Caught : ",e)

'''
except ZeroDivisionError as e:
    print("Exception Caught",e)

except ValueError as e:
    print("Exception Caught",e)
'''


    
print("End Code")
