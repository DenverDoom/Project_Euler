def ranges_for_n_digits(n):
    start = 10**n - 1
    end = 10**(n-1) - 1
    return (start, end)
def max_palin_n_digits(n):
    palin_list = list()
    for i in range(ranges_for_n_digits(n)[0],ranges_for_n_digits(n)[1],-1):
        for j in range(ranges_for_n_digits(n)[0],ranges_for_n_digits(n)[1], -1):
            temp_num = i * j
            str_temp_num = str(temp_num)
            rev_str_temp_num = reversed(str_temp_num)
            if (list(str_temp_num) == list(rev_str_temp_num)):
                palin_list.append(temp_num)
    return max(palin_list)

print(max_palin_n_digits(3))