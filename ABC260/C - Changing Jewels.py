N, X, Y = map(int, input().split())
DP = [[0, 0] for _ in range(N)]
DP[N - 1][0] = 1
for i in range(N - 1, 0, -1):
    DP[i - 1][0] += DP[i][0]
    DP[i][1] += DP[i][0] * X
    DP[i][0] = 0
    DP[i - 1][0] += DP[i][1]
    DP[i - 1][1] += DP[i][1] * Y
    DP[i][1] = 0
print(DP[0][1])
