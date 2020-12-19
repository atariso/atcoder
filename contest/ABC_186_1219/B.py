import numpy as np

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

summation = sum(map(sum, a))
minimum = min(map(min, a))

print(summation - h * w * minimum)