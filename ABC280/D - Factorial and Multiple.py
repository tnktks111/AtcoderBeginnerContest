import math
from collections import defaultdict
from bisect import bisect_left
N = int(input())
def prime_factorization(x:int) -> dict:
    for i in range(2, math.floor(math.sqrt(x)) + 1):
        if x % i == 0:
            res = prime_factorization(x // i)
            res[i] = res.get(i, 0) + 1
            return res
    res = defaultdict(int)
    res[x] += 1
    return res

def cnt_factor(x:int, total:int) -> int:
    cur = x
    res = 0
    while total >= cur:
        res += total // cur
        cur *= x
    return (res)

def required_num_to_include_x_factor(factor:int, num:int) -> int:
    ng = -1
    ok = num
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if cnt_factor(factor, factor * mid) >= num:
            ok = mid
        else:
            ng = mid
    return ok * factor

res = 1
for k, v in prime_factorization(N).items():
    res = max(required_num_to_include_x_factor(k, v), res)
print(res)
