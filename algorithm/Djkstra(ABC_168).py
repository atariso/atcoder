from heapq import heappush, heappop

INF = 10 ** 9


def dijkstra(s, n):  # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]:  # ノード v に隣接しているノードに対して
            if seen[to] is False \
                    and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


n, m = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(m)]
adj = [[] for _ in range(n+1)]
for n1, n2 in edge:
    adj[n1] += [(n2, 1)]
    adj[n2] += [(n1, 1)]

print(adj)
d = dijkstra(1, n+1)

print(d)