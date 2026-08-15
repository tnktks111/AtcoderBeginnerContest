# 裏の発想
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)

def stack_dfs(start:int) -> int:
    stack = [start]
    res = 0
    seen = set([start])
    while stack:
        cur = stack.pop()
        for nei in G[cur]:
            if nei in seen:
                continue
            seen.add(nei)
            stack.append(nei)
            res += 1
    return res

res = 0
for i in range(N):
    res += stack_dfs(i)
res -= M
print(res)