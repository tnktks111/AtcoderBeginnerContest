N = int(input())
INF = float("inf")
adj = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    adj[a].append(b)
    adj[b].append(a)

ranges = [[INF, -INF] for _ in range(N)]
def iterative_dfs(root:int):
    stack = [root]
    parents = [-1] * N
    seen = set()
    last_max = 1
    while stack:
        cur = stack.pop()
        if cur not in seen:
            stack.append(cur)
            seen.add(cur)
            for nei in adj[cur]:
                if nei == parents[cur]:
                    continue
                parents[nei] = cur
                stack.append(nei)
        else:
            for nei in adj[cur]:
                if nei == parents[cur]:
                    continue
                ranges[cur][0] = min(ranges[cur][0], ranges[nei][0])
                ranges[cur][1] = max(ranges[cur][1], ranges[nei][1])
            if ranges[cur][0] == INF and ranges[cur][1] == -INF:
                ranges[cur][0] = last_max
                ranges[cur][1] = last_max
                last_max += 1

iterative_dfs(0)

for l, r in ranges:
    print(l, r)


