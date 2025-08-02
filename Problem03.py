from sympy import *

def largest_prime_factor(num):
    prime_factor_list = [2]
    end = int(num ** 0.5)
    for i in range(1,end,2):
        if(num % i == 0):
            if(isprime(i) == True):
                prime_factor_list.append(i)
    return max(prime_factor_list)

num = 600851475143
print(largest_prime_factor(num))