from math import sqrt
f = open("p042_words.txt", "r")
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
count = 0
for i in name_str:
    sumWord = 0
    for j in i:
        f = ord(j) - 64
        sumWord = sumWord + f
    triTerm = (sqrt(1 + 4 * 2 * sumWord) - 1)/2
    if(triTerm - int(triTerm)) == 0:
        count = count + 1
print(count)