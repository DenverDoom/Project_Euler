num = pow(2,1000)
num_str = str(num)
sum = 0
for x in num_str:
    x_int = int(x)
    sum = sum + x_int

print(sum)