# A
n = int(input())
s = input()
t = input()


def dup_length(s, t):
    longest = 0
    for i in range(len(t) - 1, -1, -1):
        sub_s = s[i:]
        sub_t = t[:len(sub_s)]
        if sub_s == sub_t:
            longest = len(sub_t)
    return longest


d_len = dup_length(s, t)
if len(s) + len(t) - d_len >= n:
    print(len(s) + len(t) - d_len)
else:
    print(len(s) + len(t))
