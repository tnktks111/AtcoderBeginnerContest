import heapq

N, M = map(int, input().split())

events = [tuple(map(int, input().split())) for _ in range(M)]

res = [0] * N

waitq = list(range(N))
recover = []

for i, (t, w, s) in enumerate(events):
    # 復帰処理
    while recover and recover[0][0] <= t:
        heapq.heappush(waitq, recover[0][1])
        heapq.heappop(recover)

    if not waitq:
        continue

    nxt = heapq.heappop(waitq)
    res[nxt] += w
    heapq.heappush(recover, (t + s, nxt))

print(*res, sep="\n")
