N, K = map(int, input().split())
A = list(map(int, input().split()))

# ダブリング
# dp[i][j] ... 皿の中身がj(modN)である状態から2^i回操作したあとの皿の枚数の増加分
# dp[0][j] = A[j]
# dp[i][j] = dp[i - 1][(j + dp[i - 1][j])(mod N)](後半の増分) + dp[i - 1][j](前半の増分)

dp = [[0] * N for _ in range(40)]

for j in range(N):
    dp[0][j] = A[j]

for i in range(1, 40):
    for j in range(N):
        dp[i][j] = dp[i - 1][(j + dp[i - 1][j]) % N] + dp[i - 1][j]

cur = 0
i = 0
while K:
    if K & 1:
        cur += dp[i][cur % N]
    K >>= 1
    i += 1

print(cur)

