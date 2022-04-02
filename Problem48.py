n = 1000
sumTot = 0
for i in range (1, n+1):
    sumTot = sumTot + pow(i,i)

sum_str = str(sumTot)
print(sum_str)
print(sum_str[-10:])