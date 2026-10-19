import math
from itertools import accumulate

N, Q = map(int, input().split())
A = list(map(int, input().split()))

acc = [0] + list(accumulate(A))
tri_acc = [0] * (N + 1)

for i in range(1, N + 1):
    tri_acc[i] = tri_acc[i - 1] + acc[i]

# print(acc)
# print(tri_acc)

def solve(k: int):
    if k == 0:
        return 0
    l_min = math.ceil(math.sqrt(2 * k) - 1)
    l_max = math.floor(math.sqrt(2 * k) + 1)

    # print(k, l_min, l_max)
    for m in range(l_min, l_max + 1):
        if m * (m - 1) < 2 * k and 2 * k <= m * (m + 1):
            l = m
            break

    assert l is not None
    # print("l:", l, "k:", k)
    return tri_acc[l - 1] + acc[k - l * (l - 1) // 2]

for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    print(solve(r) - solve(l))