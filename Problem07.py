from sympy import *

limit = 10001
num = 1
prev_prime = 0
counter = 0
while(counter <= limit-1):
    num += 1
    if(isprime(num)):
        prev_prime = num
        counter += 1

print(prev_prime)