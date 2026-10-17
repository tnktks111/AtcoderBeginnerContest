import sys
sys.setrecursionlimit(10 ** 6)
from itertools import accumulate

N = int(input())
adj = [[] for _ in range(N)]

edges = []
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    edges.append((a, b))
    adj[a].append(b)
    adj[b].append(a)

in_arr = [-1] * N
out_arr = [-1] * N
tour = []

def dfs(cur:int, parent:int):
    in_arr[cur] = len(tour)
    tour.append(cur)
    for nei in adj[cur]:
        if nei == parent:
            continue
        dfs(nei, cur)
    out_arr[cur] = len(tour)

dfs(0, -1)

results_tour = [0] * (N + 1)
for i, (u, v) in enumerate(edges, start=1):
    if in_arr[u] > in_arr[v]:
        u, v = v, u
    v_subtree_size = out_arr[v] - in_arr[v]
    u_subtree_size = N - v_subtree_size
    if v_subtree_size > u_subtree_size:
        results_tour[in_arr[v]] += i
        results_tour[out_arr[v]] -= i
    else:
        results_tour[0] += i
        results_tour[in_arr[v]] -= i
        results_tour[out_arr[v]] += i
        results_tour[-1] -= i

results_tour = list(accumulate(results_tour))[:-1]

results = [0] * N
for i in range(N):
    results[tour[i]] = results_tour[i]

print(*results)