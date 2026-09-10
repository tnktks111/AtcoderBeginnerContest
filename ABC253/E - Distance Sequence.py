N, M, K = map(int, input().split())
MOD = 998244353

dp = [[0] * (M + 1) for _ in range(N)]

for j in range(1, M + 1):
    dp[0][j] = dp[0][j - 1] + 1

for i in range(1, N):
    for j in range(1, M + 1):
        dp[i][j] = dp[i][j - 1]
        dp[i][j] += dp[i - 1][M]
        dp[i][j] %= MOD
        l = max(j - K, 0)
        r = min(j + K - 1, M)
        if r <= l:
            continue
        dp[i][j] -= (dp[i - 1][r] - dp[i - 1][l])
        dp[i][j] %= MOD
print(dp[-1][-1])
