import heapq
A = int(input())

minHeap = []
addNum = 0

for i in range(A):
    q = list(map(int, input().split()))
    if (q[0] == 1):
        heapq.heappush(minHeap, q[1] - addNum)
    elif (q[0] == 2):
        addNum += q[1]
    else:
        print(heapq.heappop(minHeap) + addNum)