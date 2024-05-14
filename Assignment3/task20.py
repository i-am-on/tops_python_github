'''
task-20. Write python program that user to enter only odd numbers, else will 
raise an exception.
'''

while True:
    try:
        num = int(input("Please enter an odd number: "))

        if num%2!=0:
            print("You entered odd number:", num)
            break

        else:
            raise ValueError("You must enter an odd number.")

    except ValueError as e:
        print(e)
