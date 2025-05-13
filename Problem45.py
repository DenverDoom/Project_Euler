def hexagon_number(n):
    return n * (2 * n - 1)


def is_pentagon_number(num):
    n = (1 + (1 + 24 * num) ** 0.5) / 6
    n_int = int(n)
    if n == n_int:
        return True
    else:
        return False


limit = 30000
tri_penta_hexa_list = []
for i in range(144, limit):
    temp = hexagon_number(i)
    if is_pentagon_number(temp):
        tri_penta_hexa_list.append(temp)
        print(f'Found Triangle Number: {temp}')
        break
    else:
        print(f'Not found for {i}')

print(tri_penta_hexa_list)