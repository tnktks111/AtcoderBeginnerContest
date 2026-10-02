"""
...
..o
...

111
120
121
"""


H, W, N = map(int, input().split())

holes = set(tuple(map(int, input().split())) for _ in range(N))

dp = [[0] * (W + 1) for _ in range(H + 1)]

res = 0
for h in range(1, H + 1):
    for w in range(1, W + 1):
        if (h, w) in holes:
            continue
        dp[h][w] = min(dp[h - 1][w], dp[h][w - 1], dp[h - 1][w - 1]) + 1
        res += dp[h][w]

print(res)


