# %%

import math


def combination(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def main():
    length = int(input())
    return combination(length - 1, 11)


if __name__ == '__main__':
    message = main()
    print(message)
