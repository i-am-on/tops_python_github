'''
Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings.
'''

string_list = ["abc", "xyz", "aba", "1221", "aa"]

count = 0

for i in string_list:
    
    if len(i) >= 2 and i[0] == i[-1]:
        
        count += 1

print("Number of strings with same first and last character:", count)
