d1 = {"a":10, "b":20, "c":30}
d2 = {"b":40, "c":50, "d":60}
d3 = {}

for i in d1:
    if i in d2:
        d3[i] = d1[i]+d2[i]
    else:
        d3[i] = d1[i]

print(d3)
