num = 100
factorial = 1
for i in range (1, num+1):
    factorial = factorial*i
factorial_str = str(factorial)
sum = 0
for x in factorial_str:
    x_int = int(x)
    sum = sum + x_int

print(sum)