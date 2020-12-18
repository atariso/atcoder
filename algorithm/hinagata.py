# %%
def execute():
    a, b, c, x, y = map(int, input().split())


if __name__ == '__main__':
    message = execute()
    print(exec())

# %%
def exec():
    n = int(input())
    a = [[map(int, input().split())] for _ in range(n)]


if __name__ == '__main__':
    message = exec()
    print(exec())

# %%
# dp
from functools import lru_cache


@lru_cache(maxsize=None)
def dp(a, b, c):
    pass

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(dp(a, b, c))

# %%
# bit全探索
def exec():
    n = int(input())
    for i in range(2 ** n):
        bag = []
        print("pattern {}: ".format(i), end="")
        for j in range(n):  # このループが一番のポイント
            if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
                bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
        print(bag)


if __name__ == '__main__':
    message = exec()
    print(exec())

