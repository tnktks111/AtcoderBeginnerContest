from collections import defaultdict
from itertools import accumulate
import bisect
N, M, C = map(int, input().split())
A = list(map(int, input().split()))
cnt = defaultdict(int)
for i in range(N):
    if A[i] == 0:
        cnt[M] += 1
    else:
        cnt[A[i]] += 1

A_set = sorted(list(cnt.keys()))
A_cumsum = [cnt[a] for a in A_set]
A_cumsum = A_cumsum[:] + A_cumsum[:]
A_cumsum = list(accumulate(A_cumsum))
res = 0
if A_set[-1] != M:
    A_set.append(M)
# print(A_cumsum)
# print(A_set)
for i in range(len(A_set)):
    if i == 0:
        times = A_set[i] - 0
        start = 0
    else:
        times = A_set[i] - A_set[i - 1]
        start = A_cumsum[i - 1]
    res += (A_cumsum[bisect.bisect_left(A_cumsum, start + C)] - start) * times
    # print(tmp)
print(res)