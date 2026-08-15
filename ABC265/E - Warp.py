MOD = 998244353
N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())

blocked = set(list(tuple(map(int, input().split())) for _ in range(M)))
dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0][0] = 1
for n in range(1, N + 1):
    for x in range(0, n + 1):
        for y in range(0, n - x + 1):
            z = n - x - y
            if (A * x + C * y + E * z, B * x + D * y + F * z) in blocked:
                continue
            dp[n][x][y] += dp[n - 1][x][y]
            dp[n][x][y] %= MOD
            if x - 1 >= 0:
                dp[n][x][y] += dp[n - 1][x - 1][y]
                dp[n][x][y] %= MOD
            if y - 1 >= 0:
                dp[n][x][y] += dp[n - 1][x][y - 1]
                dp[n][x][y] %= MOD
res = 0
for i in range(N + 1):
    for j in range(N + 1):
        res += dp[N][i][j]
        res %= MOD
print(res) 