N = int(input())
mod = 998244353
dp = [[0] * 9 for _ in range(N)]
res = 0
for c in range(9):
    dp[0][c] = 1
for r in range(N - 1):
    for c in range(9):
        dp[r+1][c] = dp[r][c]
        if c > 0:
            dp[r+1][c] = (dp[r + 1][c] + dp[r][c - 1]) % mod
        if c < 8:
            dp[r+1][c] = (dp[r + 1][c] + dp[r][c + 1]) % mod
for c in range(9):
    res += dp[N-1][c]
print(res % mod)