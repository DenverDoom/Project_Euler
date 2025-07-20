F1, F2 = 1, 1
count = 2


def count_digits(number):
    return len(str(number))


while True:
    nth = F1 + F2
    count = count + 1
    if count_digits(nth) < 1000:
        F1 = F2
        F2 = nth
    else:
        break

print(count)
