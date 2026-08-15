import heapq

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
mathQ = []
engQ = []
totalQ = []
res = set()
for i in range(N):
    mathQ.append((-A[i], i + 1))
    engQ.append((-B[i], i + 1))
    totalQ.append((-A[i]-B[i], i + 1))
heapq.heapify(mathQ)
heapq.heapify(engQ)
heapq.heapify(totalQ)
for _ in range(X):
    _, idx = heapq.heappop(mathQ)
    res.add(idx)
while Y:
    _, idx = heapq.heappop(engQ)
    if idx not in res:
        res.add(idx)
        Y -= 1
while Z:
    _, idx = heapq.heappop(totalQ)
    if idx not in res:
        res.add(idx)
        Z -= 1
res = list(res)
res.sort()
for num in res:
    print(num)