# C
import math

n = int(input())
counter = 0

for i in range(1, n):
    counter += (n - 1) // i

print(counter)
