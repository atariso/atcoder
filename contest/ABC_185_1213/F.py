# %%
from sys import stdin

input = stdin.readline


def execute():
    n, q = map(int, input().split())
    a_n = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(q)]

    for t, x, y in query:
        if t == 1:
            # a_xiをa_xi xor y_i で置き換え
            # a_n[x] = int(bin(a_n[x]) ^ bin(y), 2)
            a_n[x - 1] = a_n[x - 1] ^ y
        elif t == 2:
            xor_product = a_n[x - 1]
            for i in range(x, len(a_n)):
                xor_product = xor_product ^ a_n[i]
            print(xor_product)


if __name__ == '__main__':
    message = execute()

