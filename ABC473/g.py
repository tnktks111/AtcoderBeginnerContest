from functools import cache
import sys
sys.setrecursionlimit(10 ** 6)

N, K = map(int, input().split())
MOD = 998244353

inv_nums = [pow(i, MOD - 2, MOD) for i in range(N + 1)]

@cache
def dfs(n, k):
    if n == 1 and k == 1:
        return 1
    elif k <= 1:
        return 0
    return (dfs(n - 1, k - 1) * inv_nums[n] % MOD + (n - 1) * dfs(n - 1, k - 2) * inv_nums[n] % MOD) % MOD

print(dfs(N, K))