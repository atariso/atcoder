import re

s = input()
k = int(input())


def nchars(s, n):
    assert n > 0
    reg = re.compile("(.)\\1{%d,}" % (n - 1))
    while True:
        m = reg.search(s)
        if not m:
            break
        yield m.group(0)
        s = s[m.end():]


def get_sum_seqence(_s):
    seq = list(nchars(_s, 2))
    count_seq = list(map(len, seq))

    summation = 0
    for c in count_seq:
        if c > 1:
            summation += c // 2
    return summation


if len(s) == 1:
    print(k // 2)
elif len(list(nchars(s, 1))) == 1:
    print((len(s) * k) // 2)
elif s[0] != s[-1]:
    print(get_sum_seqence(s) * k)
else:
    if get_sum_seqence(s) * 2 == get_sum_seqence(s + s):
        print(get_sum_seqence(s) * k)
    else:
        print(get_sum_seqence(s) * k + k - 1)
