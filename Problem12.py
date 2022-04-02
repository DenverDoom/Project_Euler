def countDivisor(triNumber):
    divisors = []
    for i in range (1, triNumber+1):
        if triNumber % i == 0:
            divisors.append(i)
    print(len(divisors))
    return len(divisors)

n = 99999999
outPut = 1
for i in range(1,n+1):
    triNumber = i * (i + 1) // 2
    if countDivisor(triNumber) > 500:
        outPut = triNumber
        break
print(outPut)