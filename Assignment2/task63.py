'''
Write a Python program to returns sum of all divisors of a number
'''

number = int(input("Enter a number: "))

sum = 0

for i in range(1, number + 1):
    if number % i == 0:
        sum += i

print("The sum of all divisors of", number, "is : ", sum)
