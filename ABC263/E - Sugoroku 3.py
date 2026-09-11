N = int(input())
A = list(map(int, input().split()))
INF = float("inf")
MOD = 998244353

dp = [INF] * (N + 1)
dp[N-1] = 0
dp[N] = 0

for i in range(N - 2, -1, -1):
    inv = pow(A[i], MOD - 2, MOD)
    inv_plus_one = pow(A[i] + 1, MOD - 2, MOD)
    dp[i] = 1
    dp[i] += (dp[i + 1] - dp[i + A[i] + 1]) * inv_plus_one
    dp[i] %= MOD
    dp[i] *= (1 + inv)
    dp[i] %= MOD
    dp[i] += dp[i + 1]
    dp[i] %= MOD

print((dp[0] - dp[1]) % MOD)
