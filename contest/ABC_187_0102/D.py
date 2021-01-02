n = int(input())
abn = [list(map(int, input().split())) for _ in range(n)]
info_n = []
sum_aoki = 0
for ab in abn:
    c = ab[0] + ab[1]
    d = ab[0] * 2 + ab[1]
    info_n.append([ab[0], ab[1], c, d])
    sum_aoki += ab[0]

info_n = sorted(info_n, key=lambda x: x[3], reverse=True)
count = 0
vote_t = 0
vote_a = sum_aoki
for info in info_n:
    vote_t += info[2]
    vote_a -= info[0]
    count += 1
    if vote_t > vote_a:
        break
print(count)
