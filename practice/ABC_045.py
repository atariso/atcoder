# B
sa = list(input())
sb = list(input())
sc = list(input())

turn = 0
end = False
while not end:
    if turn == 0:
        while turn == 0:
            if len(sa) == 0:
                end = True
                break
            a = sa.pop(0)
            if a == 'a':
                continue
            elif a == 'b':
                turn = 1
            elif a == 'c':
                turn = 2
    elif turn == 1:
        while turn == 1:
            if len(sb) == 0:
                end = True
                break
            b = sb.pop(0)
            if b == 'b':
                continue
            elif b == 'a':
                turn = 0
            elif b == 'c':
                turn = 2
    elif turn == 2:
        while turn == 2:
            if len(sc) == 0:
                end = True
                break
            c = sc.pop(0)
            if c == 'c':
                continue
            elif c == 'a':
                turn = 0
            elif c == 'b':
                turn = 1

if turn == 0:
    print('A')
elif turn == 1:
    print('B')
elif turn == 2:
    print('C')
