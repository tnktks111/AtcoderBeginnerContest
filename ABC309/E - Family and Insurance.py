import heapq

N, M = map(int, input().split())


adj = [[] for _ in range(N)]
parents = list(map(lambda x: int(x) - 1, input().split()))

for i in range(1, N):
    adj[parents[i - 1]].append(i)

maxq = []
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    maxq.append((-y, x))

heapq.heapify(maxq)

seen = [False] * N
while maxq:
    remain, cur = heapq.heappop(maxq)
    remain *= -1
    if seen[cur]:
        continue
    seen[cur] = True
    if remain > 0:
        for nei in adj[cur]:
            if seen[nei]:
                continue
            heapq.heappush(maxq, (-(remain - 1), nei))

res = 0
for i in range(N):
    if seen[i]:
        res += 1

print(res)