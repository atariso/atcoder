n, w = map(int, input().split())
stp = [map(int, input().split()) for _ in range(n)]
usage = [0] * (2 * 10 ** 5)

for s, t, p in stp:
    usage[s] += p
    usage[t] -= p
use = 0
for u in usage:
    usage += u
    print(usage)