from collections import defaultdict
from itertools import accumulate

N, Q = map(int, input().split())

num2intervals = defaultdict(list)
imos = [0] * (N + 1)

for _ in range(Q):
    l, r, x = map(int, input().split())
    l -= 1
    num2intervals[x].append((l, r))

for num, intervals in num2intervals.items():
    merged_intervals = []
    prv = None
    for l, r in sorted(intervals):
        if prv is None:
            prv = [l, r]
        elif prv[1] < l:
            merged_intervals.append(tuple(prv))
            prv = [l, r]
        else:
            prv[1] = max(r, prv[1])
    if prv is not None:
        merged_intervals.append(prv)

    # print(num)
    # print("before:", intervals)
    # print("after :", merged_intervals)
    for l, r in merged_intervals:
        imos[l] += 1
        imos[r] -= 1

res = list(accumulate(imos))
print(*res[:-1])