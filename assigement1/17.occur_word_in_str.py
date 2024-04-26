s = "Hello World! Hello"
s = s.split()

i=0
count=0

while i<len(s):
    count=0
    for j in s:
        if s[i]==j:
            count = count+1
    
    print(s[i],"present in string",count,"time")
    i = i+1
        
