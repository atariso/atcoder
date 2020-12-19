N = int(input())


def base_n(x, n):
    if int(x / n):
        return base_n(int(x / n), n) + str(x % n)
    return str(x % n)


counter = 0
for i in range(1, N + 1):
    i_str: str = str(i)
    oct_i_str: str = base_n(i, 8)
    if '7' not in oct_i_str and '7' not in i_str:
        counter += 1
print(counter)
