a,b=0,1
n = int(input("Enter number:"))


print(a,b, end=' ')

for i in range(n):
    print(b, end=' ')
    a,b =b,a+b
    
    #a=b
    #b=c

