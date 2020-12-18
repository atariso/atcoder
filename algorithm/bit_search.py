# bit全探索
def bit_search():
    n, m = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(m)]
    max_person_num = 0
    for i in range(2 ** n):
        habatsu = []
        for j in range(n):
            if (i >> j) & 1:  # shift right and check
                habatsu.append(j)
        from itertools import combinations

        if len(habatsu) < 2:
            continue

        is_able_to_make = True
        for combi in combinations(habatsu, 2):
            ok = False
            for kankei in xy:
                if kankei[0] == combi[0] and kankei[1] == combi[1]:
                    ok = True
                elif kankei[0] == combi[1] and kankei[1] == combi[0]:
                    ok = True
            if not ok:
                is_able_to_make = False
                break

        if is_able_to_make:
            if max_person_num <= len(habatsu):
                max_person_num = len(habatsu)
    return max_person_num


if __name__ == '__main__':
    message = bit_search()
    print(message)