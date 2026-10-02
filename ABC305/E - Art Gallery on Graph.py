import heapq

N, M, K = map(int, input().split())

adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    adj[a].append(b)
    adj[b].append(a)

maxq = []
result = [False] * N

for _ in range(K):
    p, h = map(int, input().split())
    p -= 1
    maxq.append((-h, p))

heapq.heapify(maxq)

while maxq:
    remain, cur = heapq.heappop(maxq)
    if result[cur]:
        continue
    result[cur] = True
    remain *= -1
    if remain > 0:
        for nei in adj[cur]:
            if result[nei]:
                continue
            heapq.heappush(maxq, (-(remain - 1), nei))

res = []
for i in range(N):
    if result[i]:
        res.append(i + 1)

print(len(res))
print(*res)