import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())

degree = [0] * N
adj = [[] for _ in range(N)]
seen = [False] * N

for _ in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    adj[u].append(v)
    adj[v].append(u)
    degree[u] += 1
    degree[v] += 1

res = []
def dfs(start: int):
    # print(f"start: {start}")
    center = None
    seen[start] = True
    for nei in adj[start]:
        if seen[nei]:
            continue
        center = nei
        break
    if center is None:
        return
    seen[center] = True
    # print(f"center: {center}")
    res.append(len(adj[center]))
    for nei in adj[center]:
        if len(adj[nei]) == 1:
            continue
        # print(nei, adj[nei])
        assert len(adj[nei]) == 2
        seen[nei] = True
        for neinei in adj[nei]:
            if neinei == center:
                continue
            dfs(neinei)

for i in range(N):
    if degree[i] == 1:
        dfs(i)
        break

res.sort()
print(*res)
