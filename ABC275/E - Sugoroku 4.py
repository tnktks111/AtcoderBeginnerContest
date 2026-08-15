N, M, K = map(int, input().split())
MOD = 998244353
INV_M = pow(M, MOD - 2, MOD)
dp = [[0] * (N + 1) for _ in range(K + 1)]
for i in range(K + 1):
    dp[i][0] = 1
for i in range(1, K + 1):
    for j in range(1, N + 1):
        for m in range(1, M + 1):
            dp[i][j] += dp[i - 1][abs(j - m)] * INV_M
            dp[i][j] %= MOD
print(dp[K][N])