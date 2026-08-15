from collections import defaultdict, deque
N = int(input())

G = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

q = deque([1])
seen = set()
res = 1
while q:
    cur = q.popleft()
    res = max(cur, res)
    for nei in G[cur]:
        if nei in seen:
            continue
        q.append(nei)
        seen.add(nei)
print(res)

    