f = open("p022_names.txt", "r")
name = []
for x in f:
    name = x.split(',')
name_str = []
for i in name:
    ind = 0
    s = i.split('\"')
    name_str.insert(ind,s[1])
    ind = ind + 1
name_str.sort()
mulSum = 0
for i in name_str:
    sum = 0
    for j in i:
        f = ord(j) - 64
        sum = sum + f
    mulSum = mulSum + sum * (name_str.index(i)+1)
print(mulSum)