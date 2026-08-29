N, M = map(int, input().split())
INF = float("inf")

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b, c))

dist = [[INF] * N for _ in range(N)]

for u, v, w in edges:
    dist[u][v] = w
    dist[v][u] = w

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

res = 0
for i, j, w in edges:
    for k in range(N):
        if w >= dist[i][k] + dist[k][j]:
            res += 1
            break

print(res)