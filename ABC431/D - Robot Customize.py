N = int(input())
WHB = [tuple(map(int, input().split())) for _ in range(N)]
weight_max = 0
for i in range(N):
    weight_max += WHB[i][0]
weight_max //= 2
dp = [[0] * (weight_max + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    Weight, Head, Body = WHB[i - 1]
    for w in range(weight_max + 1):
        dp[i][w] = dp[i - 1][w] + Body
        if w - Weight >= 0:
            dp[i][w] = max(dp[i][w], dp[i - 1][w - Weight] + Head)
print(dp[N][weight_max])