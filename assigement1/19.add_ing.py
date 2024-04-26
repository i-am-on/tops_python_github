s = "Hello World"

if len(s)<=3:
    print(s)
elif len(s)>3 and s[len(s)-3:]!="ing":
    print(s+"ing")   
elif len(s)>3 and s[len(s)-3:]=="ing":
    print(s+"ly")
