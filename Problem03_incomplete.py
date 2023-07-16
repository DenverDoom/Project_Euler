from sympy import *

def largest_prime_factor(num):
    prime_factor_list = [2]
    for i in range(1,num//2,2):
        print(i)
        if(num % i == 0):
            if(isprime(i) == True):
                prime_factor_list.append(i)
    return max(prime_factor_list)

num = 600851475143
print(largest_prime_factor(num))