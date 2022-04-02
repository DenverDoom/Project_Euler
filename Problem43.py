import itertools

s = '0123456789'
nums = list(s)
permutations = list(itertools.permutations(nums))
permArr = [''.join(permutation) for permutation in permutations]
sumTot = 0
for i in permArr:
    if int(i[1:4]) % 2 == 0:
        if int(i[2:5]) % 3 == 0:
            if int(i[3:6]) % 5 == 0:
                if int(i[4:7]) % 7 == 0:
                    if int(i[5:8]) % 11 == 0:
                        if int(i[6:9]) % 13 == 0:
                            if int(i[7:10]) % 17 == 0:
                                sumTot = sumTot + int(i)

print(sumTot)