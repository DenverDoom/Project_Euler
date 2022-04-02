
def leftTruncatedPrimes(p):
    p_str = str(p)
    length = len(p_str)
    flag = True
    if p_str[-1] == '1':
        flag = False
    else:
        for i in range(1,length):
            c = p_str[-(length-i):]
            c_int = int(c)
            if (c_int == 2 or c_int == 3 or c_int == 5 or c_int == 7) and len(c) > 1: # and length of c greater than 1
                flag = False
                break
            for j in range(2,int(sqrt(c_int))+1):
                if c_int % j == 0:
                    flag = False
                    break
                else:
                    flag = True
    return flag

from math import sqrt
def rightTruncatedPrimes(p):
    p_str = str(p)
    length = len(p_str)
    flag = True
    if p_str[0] == '1':
        flag = False
    else:
        for i in range(1,length):
            c = p_str[0:length-i]
            c_int = int(c)
            print(i, c, c_int)
            if (c_int == 2 or c_int == 3 or c_int == 5 or c_int == 7) and len(c) > 1: # and length of c greater than 1
                flag = False
                break
            else:
                for j in range(2,int(sqrt(c_int))+1):
                    if c_int % j == 0:
                        flag = False
                        break
                    else:
                        flag = True
    return flag
print(rightTruncatedPrimes(5023))
n = 10000
sum = 0
limit = 0
for i in range(10,n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            if (leftTruncatedPrimes(i) == True) and (rightTruncatedPrimes(i) == True):
                sum = sum + i
                print(i)
                limit = limit + 1
                if limit == 100:
                    break

print(sum)