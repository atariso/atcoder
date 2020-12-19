n = int(input())
a = map(int, input().split())
a = sorted(a)

sum_a = sum(a)
discarded = 0
accum_diff = 0
for idx, a_i in enumerate(a):
    accum_diff += sum_a - (len(a) - idx) * a_i - discarded
    discarded += a_i

print(accum_diff)