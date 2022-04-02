import math
def isPrime(n):
    flag = False
    for i in range(2, (int)(math.sqrt(n))+1):
        if n % i == 0:
            flag = True
            break
    print(flag)
    return flag

sum = 0
for i in range(2, 2000000):
    if isPrime(i) == False:
        sum+=i

print(sum)