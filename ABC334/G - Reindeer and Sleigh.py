from itertools import accumulate
from bisect import bisect_left

N, Q = map(int, input().split())
R = list(map(int, input().split()))
R.sort()

acc_r = list(accumulate(R))
# print(acc_r)

for _ in range(Q):
    q = int(input())
    i = bisect_left(acc_r, q)
    if i >= N:
        print(N)
    elif acc_r[i] == q:
        print(i + 1)
    else:
        print(i)