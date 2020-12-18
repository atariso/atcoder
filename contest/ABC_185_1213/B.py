# %%
def main():
    n, m, t = map(int, input().split())
    a_b = [list(map(int, input().split())) for _ in range(m)]
    ok = True
    battery = n

    former_b = 0
    for a, b in a_b:
        battery -= (a - former_b)
        if battery <= 0:
            ok = False
            break

        battery += (b - a)
        if battery >= n:
            battery = n
        former_b = b

    if ok:
        battery -= (t - former_b)
        if battery <= 0:
            ok = False

    if ok:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    message = main()
    print(message)
