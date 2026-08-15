from collections import defaultdict
import heapq

N, M = map(int, input().split())

indegree = [0] * N
adj = defaultdict(list)
minHeap = []

for _ in range(M):
    src, dst = map(int, input().split())
    src -= 1
    dst -= 1
    indegree[dst] += 1
    adj[src].append(dst)

minHeap = [i for i in range(N) if indegree[i] == 0]
heapq.heapify(minHeap)

res = []
while(minHeap):
    node = heapq.heappop(minHeap)
    res.append(node + 1)
    for nei in adj[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            heapq.heappush(minHeap, nei)
            
if len(res) != N:
    print(-1)
else:
    print(" ".join(map(str, res)))
