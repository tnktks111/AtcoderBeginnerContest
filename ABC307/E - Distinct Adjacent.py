N, M = map(int, input().split())
MOD = 998244353

dp = [0] * N

dp[0] = M % MOD
dp[1] = (M % MOD) * (M - 1) % MOD

for i in range(2, N):
    if i > 2:
        dp[i] = (dp[i - 1] * (M - 2) % MOD + dp[i - 2] * (M - 1) % MOD) % MOD
    else:
        dp[i] = dp[i - 1] * (M - 2) % MOD

# print(dp)

print(dp[-1])