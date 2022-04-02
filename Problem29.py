a = []
b = []
c = []
for i in range(2,101):
    a.append(i)
    b.append(i)
for i in a:
    for j in b:
        x = pow(i,j)
        c.append(x)
c = list(set(c))
print(len(c))