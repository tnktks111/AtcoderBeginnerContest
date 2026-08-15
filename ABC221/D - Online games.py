import heapq
from collections import defaultdict
N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

TtoN = defaultdict(int)
for a, b in AB:
    TtoN[a] += 1
    TtoN[a + b] -= 1

times = sorted(TtoN.items())

res = [0] * N
prev_time = None
cur_users = 0

for time, delta in times:
    if prev_time is not None and cur_users > 0:
        res[cur_users - 1] += time - prev_time
    cur_users += delta
    prev_time = time
print(*res)