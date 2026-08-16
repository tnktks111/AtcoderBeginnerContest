import heapq

Q, V = map(int, input().split())
maxq = []

for _ in range(Q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        t, w = query[1], query[2]
        heapq.heappush(maxq, t - w)
    else:
        t = query[1]
        if maxq:
            print(min(V, t - heapq.heappop(maxq)))
        else:
            print(-1)