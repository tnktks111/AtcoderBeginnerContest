import heapq
N, K, X = map(int, input().split())
A = [-a for a in list(map(int, input().split()))]
heapq.heapify(A)
for _ in range(K):
    c_max = heapq.heappop(A)
    heapq.heappush(A, min(0, c_max + X))
print(-sum(A))