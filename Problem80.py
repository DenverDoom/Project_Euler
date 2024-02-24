def root_without_deci(num, preci_digit):
    a = 5 * num
    b = 5
    limit = 10 ** (preci_digit + 1)
    while b < limit:
        if a >= b:
            a -= b
            b += 10
        else:
            a *= 100
            b = (b - b%10) * 10 + b % 10
    root = str(b)[:preci_digit]
    return root

def digit_sum(root):
    sum = 0
    for digit in root:
        sum += int(digit)
    return sum

result=0
for n in range(1,101):
    if n not in [1,4,9,16,25,36,49,64,81,100]:
        root = root_without_deci(n, 100)
        result += digit_sum(root)

print(result)