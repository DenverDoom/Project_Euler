def sumOfNaturalNums(n):
    return (n*(n+1))//2

def sumOfSqrOfNaturalNums(n):
    return (n*(n+1)*(2*n+1))//6

diff = sumOfNaturalNums(100)**2 - sumOfSqrOfNaturalNums(100)
print(abs(diff))