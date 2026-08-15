N, M = map(int, input().split())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
costs = [0] * N
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
    costs[u] += A[v]
    costs[v] += A[u]

def cost_is_lower_than(c:int) -> bool:
    costs_tmp = costs[:]
    stack = []
    for i in range(N):
        if costs_tmp[i] <= c:
            stack.append(i)
    deleted = 0
    seen = set(stack)
    while stack:
        u = stack.pop()
        deleted += 1
        for nei in G[u]:
            costs_tmp[nei] -= A[u]
            if nei in seen:
                continue
            if costs_tmp[nei] <= c:
                stack.append(nei)
                seen.add(nei)
    return True if deleted == N else False
ok = max(A) * N
ng = -1

while ok - ng > 1:
    mid = (ok + ng) // 2
    if cost_is_lower_than(mid):
        ok = mid
    else:
        ng = mid

print(ok)