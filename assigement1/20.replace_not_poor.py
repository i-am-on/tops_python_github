string = input("Enter any string : ")

sn = string.find("not")
sp = string.find("poor")

if sp>sn and sn>0 and sp>0:
    string=string.replace(string[sn:(sp+4)],"good")
    print(string)
else:
    print(string)
