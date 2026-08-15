from collections import defaultdict
from sortedcontainers import SortedList
G = defaultdict(lambda: SortedList())
N, M = map(int, input().split())
for _ in range(M):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)
for i in range(1, N + 1):
    print(len(G[i]), *G[i])