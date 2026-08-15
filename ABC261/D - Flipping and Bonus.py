from collections import defaultdict
N, M = map(int, input().split())
X = list(map(int, input().split()))
bonus = defaultdict(int)
for _ in range(M):
    c, y = map(int, input().split())
    bonus[c] = y

DP = [[-float("inf")] * (N + 1) for _ in range(N + 1)]
DP[0][0] = 0
for i in range(1, N + 1):
    for j in range(N + 1):
        if j == 0:
            DP[i][j] = max(DP[i - 1])
        else:
            DP[i][j] = DP[i - 1][j - 1] + X[i - 1] + bonus[j]
print(max(DP[-1]))