sum = 1
n = 1001
oddArr = []
for i in range (3,n+1,2):
    oddArr.append(i)
sumCorner = 0
for i in oddArr:
    corner_1 = pow(i, 2)
    corner_2 = corner_1 - (i - 1)
    corner_3 = corner_2 - (i - 1)
    corner_4 = corner_3 - (i - 1)
    sumCorner = sumCorner + corner_1 + corner_2 + corner_3 + corner_4

sumTotal = sum + sumCorner

print(sumTotal)