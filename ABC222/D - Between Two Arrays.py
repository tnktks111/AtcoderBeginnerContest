from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353

dp = defaultdict(int)
dp[0] = 1

prv_max = 0
for i in range(N):
    next_dp = defaultdict(int)
    for c in range(A[i], B[i] + 1):
        if c > prv_max:
            next_dp[c] = (dp[prv_max] + next_dp[c - 1]) % MOD
        else:
            next_dp[c] = (dp[c] + next_dp[c - 1]) % MOD
    dp = next_dp
    prv_max = B[i]
    # print(dp)

print(dp[prv_max] % MOD)