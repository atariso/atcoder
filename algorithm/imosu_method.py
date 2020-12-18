# ABC1115 D - Water Heater

n, w = map(int, input().split())
lst = [0] * 3 * 10 ** 5
time_max = 0
for _ in range(n):
    s, t, p = map(int, input().split())
    lst[s] += p
    lst[t] -= p
    time_max = max(time_max, t)

flg = True
state = 0
for i in range(time_max + 1):
    state += lst[i]
    if state > w:
        flg = False
        break

if flg:
    print('Yes')
else:
    print('No')
