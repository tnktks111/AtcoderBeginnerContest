H, W = map(int, input().split())
grid = [input() for _ in range(H)]
dp = [[0] * (W + 1) for _ in range(H + 1)]
res = 0
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if grid[i - 1][j - 1] == ".":
            if not (i == j == 1) and dp[i - 1][j] == 0 and dp[i][j - 1] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = 1 + max(dp[i][j - 1], dp[i - 1][j])
                res = max(res, dp[i][j])
        else:
            dp[i][j] = 0
print(res)