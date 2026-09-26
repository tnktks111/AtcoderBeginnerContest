import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque

N, M = map(int, input().split())

adj = [deque() for _ in range(N)]
indegree = [0] * N
outdegree = [0] * N

seen = set()
for _ in range(M):
    x, y = map(lambda x: int(x) - 1, input().split())
    if (x, y) in seen:
        continue
    seen.add((x, y))
    indegree[y] += 1
    outdegree[x] += 1
    adj[x].append(y)

path = []
def dfs(cur:int):
    while adj[cur]:
        nei = adj[cur].pop()
        dfs(nei)
    path.append(cur)

start = None
end = None
for i in range(N):
    if indegree[i] == outdegree[i]:
        continue
    elif start is not None and end is not None:
        print("No")
        exit()
    elif outdegree[i] == indegree[i] + 1:
        start = i
    elif outdegree[i] + 1 == indegree[i]:
        end = i
    else:
        print("No")
        exit()

dfs(start)
res = [0] * N

path = path[::-1]

print("Yes")
for i in range(N):
    res[path[i]] = i + 1
print(*res)
