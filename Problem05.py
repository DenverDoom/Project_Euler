from sympy import *

def primes_in_range(n):
    primes = []
    for i in range(n+1):
        if(isprime(i)):
            primes.append(i)
    return(primes,n)

prime_list = primes_in_range(20)[0]

def effective_multiplier_list(ls,n):
    multipliers = []
    temp_prev = 0
    for item in ls:
        for i in range(n):
            temp_prev = pow(item, (i - 1))
            a = pow(item, i)
            temp = a
            if (temp > 20):
                break
        multipliers.append(temp_prev)
    return(multipliers)

multiplier_list = effective_multiplier_list(prime_list,primes_in_range(20)[1])

product = 1
for item in multiplier_list:
    product = product * item

print(product)