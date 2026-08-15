import heapq
from bisect import bisect_left
from collections import defaultdict
INF = float("inf")

N, M, K = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append((B, C, i + 1))
E = list(map(int, input().split()))
num_to_idx = defaultdict(list)
for i in range(K):
    num_to_idx[E[i]].append(i)

q = [(0, -1, 0)]
while q:
    prev_cost, prev_idx, u = heapq.heappop(q)
    if u == N - 1:
        print(prev_cost)
        exit()
    for v, c, road_num in G[u]:
        if not num_to_idx[road_num]:
            continue
        idx_idx = bisect_left(num_to_idx[road_num], prev_idx)
        if idx_idx == len(num_to_idx[road_num]):
            continue
        idx = num_to_idx[road_num][idx_idx]
        heapq.heappush(q, (prev_cost + c, idx, v))
print(-1)