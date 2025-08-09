import math


def calc_combination(n, r):
    return math.comb(n, r)


n = 100
count = 0
for i in range(1, n + 1):
    for j in range(0, n + 1):
        res = calc_combination(i, j)
        if res > 1000000:
            count = count + 1

print(count)
