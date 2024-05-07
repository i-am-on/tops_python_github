'''
Write a Python script to concatenate following dictionaries to create a 
new one.
'''

d = {"a":123,"b":456}
d1 = {"c":789,"d":135}
d2 = {"e":246,"f":579}

d3 = {}

d3.update(d)
d3.update(d1)
d3.update(d2)

print(d3)
