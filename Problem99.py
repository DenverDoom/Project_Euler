import math
f = open("p099_base_exp.txt", "r")
val_list = []
for i in f:
    line = i.split(',')
    base = int(line[0])
    exp = int(line[1])
    val = exp * math.log10(base)
    val_list.append(val)

print(val_list.index(max(val_list))+1)