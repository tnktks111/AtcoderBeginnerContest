import heapq
from bisect import bisect_left
from collections import defaultdict

def solve(n:int, intervals: list[tuple[int, int]]):
    i = 0
    minq = []

    Ls = list(set([interval[0] for interval in intervals]))
    Ls.sort()
    
    l2interval = defaultdict(list)
    for interval in intervals:
        l2interval[interval[0]].append(interval)

    i = 0
    while True:
        if not minq:
            nxt_idx = bisect_left(Ls, i)
            if nxt_idx == len(Ls):
                break
            i = Ls[nxt_idx]
        for interval in l2interval[i]:
            heapq.heappush(minq, interval[1])
        r = heapq.heappop(minq)
        if r < i:
            return False
        i += 1

    return True

T = int(input())
for _ in range(T):
    N = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(N)]
    if solve(N, intervals):
        print("Yes")
    else:
        print("No")
