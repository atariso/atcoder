n, k = map(int, input().split())
p = 0
exp2 = [2 ** i for i in range(20)]
# print(exp2)
c = 0
for ni in range(1, n + 1):
    multi = k / ni
    # idx = -1
    if multi <= 1:
        p += (n - c) / n
        break
    else:
        c += 1
        for idx, e2 in enumerate(exp2):
            if e2 >= multi:
                p += 1 / (n * e2)
                break
    # print('ni:{}, p:{}, multi:{}, idx:{}'.format(ni, p, multi, idx))

print(p)
