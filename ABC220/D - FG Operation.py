mod = 998244353
N = int(input())
A = list(map(int, input().split()))
dp = [[0] * 10 for _ in range(N)]
dp[0][A[0]] = 1
for i in range(N - 1):
    for j in range(10):
        if dp[i][j] != 0:
            xF = (j + A[i + 1]) % 10
            xG = (j * A[i + 1]) % 10
            dp[i+1][xF] += dp[i][j]
            dp[i+1][xG] += dp[i][j]
            dp[i+1][xF] %= mod
            dp[i+1][xG] %= mod
for i in range(10):
	print(dp[N - 1][i])
            