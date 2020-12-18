# %%
n = int(input())
h_s = [list(map(int, input().split())) for _ in range(n)]

int_max = 1 * 10 ** 4

def is_able(height, h_s_n):
    limit_n = []
    for h_s_i in h_s_n:
        limit_i = (height - h_s_i[0]) / h_s_i[1]
        limit_n.append(limit_i)
    sorted_limit_n = sorted(limit_n)

    for i in range(len(sorted_limit_n)):
        if i > sorted_limit_n[i]:
            return False
    return True


max_ = int_max
min_ = 0
mid_ = int_max // 2
found = False

while not found:
    prev_max = max_
    prev_min = min_
    prev_mid = mid_

    okay_1 = is_able(height=max_, h_s_n=h_s)
    okay_2 = is_able(height=mid_, h_s_n=h_s)
    if okay_1 and okay_2:
        max_ = mid_
        min_ = min_
        mid_ = ((max_ - min_) // 2) + min_
    elif okay_1 and not okay_2:
        max_ = max_
        min_ = mid_
        mid_ = ((max_ - min_) // 2) + min_
    elif not okay_1 and not okay_2:
        max_ = max_ * 10
        min_ = min_
        mid_ = ((max_ - min_) // 2) + min_
    # print(max_, mid_, min_)
    if max_ == prev_max and mid_ == prev_mid and min_ == prev_min:
        found = True

print(max_)
