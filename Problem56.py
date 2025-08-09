def sum_of_digits(num):
    sum = 0
    digits = [int(i) for i in str(num)]
    for i in digits:
        sum = sum + i
    return sum
a = 99
b = 99
max = 0
for i in range(1, a+1):
    for j in range(1, b+1):
        res = i ** j
        temp_sum = sum_of_digits(res)
        if temp_sum > max:
            max = temp_sum

print(max)