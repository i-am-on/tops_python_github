a = int(input("Enter any number:"))
fact=1

'''
for i in range(1,a):
    fact=fact*i
'''

for i in range(a,0,-1):
    fact=fact*i
    
print("Factorial of",a,"is:",fact)
