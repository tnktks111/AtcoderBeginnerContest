import heapq

N, M = map(int, input().split())
INF = float("inf")

adj = [[] for _ in range(N)]
v2edge = dict()

for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append((b, c))
    adj[b].append((a, c))
    v2edge[(a, b)] = i + 1
    v2edge[(b, a)] = i + 1

dist = [INF] * N
prv = [-1] * N

dist[0] = 0

minq = [(0, 0)]

while minq:
    d, cur = heapq.heappop(minq)
    if dist[cur] < d:
        continue

    for nei, w in adj[cur]:
        if dist[nei] > d + w:
            dist[nei] = d + w
            prv[nei] = cur
            heapq.heappush(minq, (d + w, nei))

res = set()
for i in range(1, N):
    res.add(v2edge[(i, prv[i])])
print(*list(res))