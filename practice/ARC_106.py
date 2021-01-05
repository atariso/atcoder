# %%
# A
n = int(input())


def search(n):
    for a in range(1, 100):
        pow3 = 3 ** a
        diff_0 = n - pow3
        if diff_0 < 5:
            return False, -1, -1
        is_int = True
        diff = diff_0
        b = 1
        while is_int:
            quo = diff // 5 ** b
            rem = diff % 5 ** b
            if quo == 1 and rem == 0:
                return True, a, b
            elif rem == 0:
                b += 1
            else:
                is_int = False


is_exist, a, b = search(n)
if is_exist:
    print(a, b)
else:
    print(-1)

# %%
# B
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
an = list(map(int, input().split()))
bn = list(map(int, input().split()))

tree = [[] for _ in range(n+1)]

for _ in range(m):
    ci, di = map(int, input().split())
    tree[ci] += [di]
    tree[di] += [ci]
