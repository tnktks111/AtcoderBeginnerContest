import heapq
from itertools import accumulate

N, Q = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = float("inf")

edges = []
for i in range(N):
    edges.append((i, (i + 1) % N, A[i]))
    edges.append(((i + 1) % N, i, A[i]))
    edges.append((i, N, B[i]))
    edges.append((N, i, B[i]))

dist = [[INF] * (N + 1) for _ in range(N + 1)]

for v in range(N + 1):
    dist[v][v] = 0

for src, to, w in edges:
    if w < dist[src][to]:
        dist[src][to] = w

for k in range(N + 1):
    for i in range(N + 1):
        if dist[i][k] == INF:
            continue
        for j in range(N + 1):
            if dist[k][j] == INF:
                continue
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for _ in range(Q):
    u, v = map(lambda x: int(x) - 1, input().split())
    print(dist[u][v])