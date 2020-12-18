# %%
def execute():
    n, m = map(int, input().split())
    a_m = list(map(int, input().split()))

    a_m = sorted(a_m)
    if m == 0:
        return 1

    a_1 = 0
    white = []
    for a_2 in a_m:
        space = a_2 - a_1 - 1
        if space != 0:
            white.append(a_2 - a_1 - 1)
        a_1 = a_2
    max_a_m = max(a_m)

    if max_a_m == n:
        pass
    else:
        white.append(n - max_a_m)

    if len(white) == 0:
        return 0
    elif max(white) == 0:
        return 0
    stamp_len = min(white)
    num = 0

    for space in white:
        if space % stamp_len == 0:
            num += space // stamp_len
        else:
            num += (space // stamp_len + 1)
    return num


if __name__ == '__main__':
    message = execute()
    print(message)
