import heapq
N = int(input())
x = list(map(int, input().split()))
dict_x = {x[i]: i for i in range(N)}
maxHeap = []
for score in x:
    heapq.heappush(maxHeap, -score)
heapq.heappop(maxHeap)
print(dict_x[-heapq.heappop(maxHeap)] + 1)