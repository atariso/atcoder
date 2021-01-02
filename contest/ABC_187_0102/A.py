ab = input().split()

sa = sum(map(int, list(ab[0])))
sb = sum(map(int, list(ab[1])))
print(max(sa, sb))
