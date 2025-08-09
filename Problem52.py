def is_all_digits_same(num_list):
    length = sorted(str(num_list[0]))
    same_len = all(sorted(str(n)) == length for n in num_list[1:])
    return same_len


def is_all_num_len_same(num_list):
    lengths = [len(str(num)) for num in num_list]
    if len(set(lengths)) == 1:
        return True
    else:
        return False


n = 99999999999999999999
for i in range(1, n + 1):
    tmp_nums = [i, 2 * i, 3 * i, 4 * i, 5 * i, 6 * i]
    if is_all_num_len_same(tmp_nums):
        if is_all_digits_same(tmp_nums):
            print(i)
            break
