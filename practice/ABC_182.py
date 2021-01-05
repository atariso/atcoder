# D
import itertools
import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 6)

n = int(input())
an = list(map(int, input().split()))

ex_max_position = []
ex_max = 0
ex_from_zero = 0
accum = list(itertools.accumulate(list(itertools.accumulate(an))))
accum = [0] + accum[:-1]

for i, a in enumerate(an):
    ex_from_zero += a
    ex_max = max(ex_max, ex_from_zero)
    ex_max_position.append(ex_max)

max_t = 0
for e, m in zip(accum, ex_max_position):
    max_t = max(max_t, e + m)

# print(accum, ex_max_position)
print(max_t)
