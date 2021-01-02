n = int(input())
xyn = [list(map(int, input().split())) for _ in range(n)]
counter = 0

for i in range(n):
    for j in range(n):
        if i >= j:
            continue
        xi = xyn[i][0]
        yi = xyn[i][1]
        xj = xyn[j][0]
        yj = xyn[j][1]
        if abs(xi - xj) >= abs(yi - yj):
            counter += 1

print(counter)