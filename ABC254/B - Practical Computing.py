N = int(input())
DP = [[0] * N for _ in range(N)]
DP[0][0] = 1
print(1)
for i in range(1, N):
    for j in range(i + 1):
        if j > 0:
            DP[i][j] = DP[i - 1][j - 1] + DP[i - 1][j]
        else:
            DP[i][j] = 1
    print(*DP[i][:i + 1])
