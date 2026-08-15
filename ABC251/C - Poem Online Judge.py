import heapq
N = int(input())
MaxHeap = []
seen = set()
for i in range(N):
    S, T = input().split()
    if S in seen:
        continue
    seen.add(S)
    MaxHeap.append((-int(T), i + 1, S))
heapq.heapify(MaxHeap)
T_neg, I, S = heapq.heappop(MaxHeap)
print(I)
