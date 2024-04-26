'''
Types of if statement

1.Simple if

  if Condition:
      Statement

2. if/else

    if condition:
        statement
    else:
        Statement

3. Nested if

    if condition:
        if condition:
            statement
        else:
            Statement
    else:
        Statement

4. Ladder if

    if condition:
        statement
    elif condition:
        Statement
    elif condition:
        Statement
    else:
        Statement
'''

'''
a=10
b=20

if a<b:
    print("A is Max")
else:
    print("B is Max")
'''

a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))

if a>b:
    if a>c:
        print("A is Max")
    else:
        print("A is not Max")
elif b>c:
        print("B is Max")
else:
    print("C is Max")











