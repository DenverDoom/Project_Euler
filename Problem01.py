def checkThreeOrFive(n):
    if(n%3 == 0 or n%5 == 0):
        return True
    else:
        return False

sums = 0
for i in range(1,1000):
    if(checkThreeOrFive(i) == True):
        sums+=i
print(sums)