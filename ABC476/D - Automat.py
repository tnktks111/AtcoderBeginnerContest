from itertools import accumulate
from bisect import bisect_right

N, M, K = map(int, input().split())

X, Y = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

A_acc = [0] + list(accumulate(A))

k_remain = Y
one_remain = X

res = 0
for i in range(M + 1):
    if i > 0:
        if k_remain * K < B[i-1]:
            continue
        k_use = (B[i-1] + K - 1) // K
        k_remain -= k_use
        one_remain += k_use * K - B[i-1]
    tmp_total = k_remain * K + one_remain
    idx = bisect_right(A_acc, tmp_total) - 1
    res = max(res, i + idx)
print(res)
