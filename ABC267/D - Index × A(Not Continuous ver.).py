N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
dp = [[-float("inf")] * (N + 1) for _ in range(M + 1)]

for i in range(N + 1):
    dp[0][i] = 0

for i in range(1, M + 1):
    for j in range(1, N + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + A[j] * i)

print(dp[-1][-1])