import heapq
N, D = map(int, input().split())
start = []
end = []
for _ in range(N):
    l, r = map(int, input().split())
    start.append([l, r])
    end.append([r, l])

heapq.heapify(start)
heapq.heapify(end)
seen = set()

punch = 0
while end:
    l, r = heapq.heappop(end)
    punch += 1
    while start and start[0][0] <= l + D - 1:
        L, R = heapq.heappop(start)
        seen.add((R, L))
    while end and tuple(end[0]) in seen:
        heapq.heappop(end)

print(punch)
