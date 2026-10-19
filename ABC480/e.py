import math

def is_lower_than_n(a:int, d:int, l:int, n:int):
    res = 1
    for i in range(l):
        res *= (a + i * d)
    return res <= n

def solve_d(a:int, l:int, n:int):
    ok = -1
    ng = 10 ** 9
    while ng - ok > 1:
        # print(ok, ng)
        mid = (ok + ng) // 2
        if is_lower_than_n(a, mid, l, n):
            ok = mid
        else:
            ng = mid
    return ok

N = int(input())
res = 0
for a in range(1, 10 ** 6):
    for l in range(3, 20):
        if pow(a, l) >= N:
            break
        max_d = solve_d(a, l, N)
        if max_d <= 0:
            continue
        res += max_d

print(res)
# print(1051148114007)