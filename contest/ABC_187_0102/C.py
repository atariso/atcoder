n = int(input())
sn = [input() for _ in range(n)]
sn = list(set(sn))
ex = []
nex = []

for s in sn:
    if s[0] == '!':
        ex.append(s[1:])
    else:
        nex.append(s)

set_ex = set(ex)
set_nex = set(nex)
isc = set_ex & set_nex

if len(isc) == 0:
    print('satisfiable')
else:
    print(isc.pop())
