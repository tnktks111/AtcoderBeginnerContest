import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

MinHeap = P[0:K - 1]
heapq.heapify(MinHeap)

heapq.heappush(MinHeap, -float("inf"))

for i in range(K - 1, N):
    heapq.heappush(MinHeap, P[i])
    heapq.heappop(MinHeap)
    print(MinHeap[0])
