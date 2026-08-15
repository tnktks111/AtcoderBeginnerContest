N, A, B, P, Q = map(int, input().split())
ROW = N - A
COL = N - B
MOD = 998244353
inv_P = pow(P, -1, MOD)
inv_PQ = pow(P * Q, -1, MOD)

dp = [[0] * COL for _ in range(ROW)]
for i in range(ROW):
    for j in range(COL):
        if i == 0:
            dp[i][j] = 1
        elif j == 0:
            if i < P:
                dp[i][j] = (P - i) * inv_P
                dp[i][j] %= MOD
            else:
                dp[i][j] = 0
        else:
            tmp = 0
            if i < P:
                tmp += (P - i) * inv_P
                tmp %= MOD
            for s in range(1, P + 1):
                for t in range(1, Q + 1):
                    if 0 <= i - s < ROW and 0 <= j - t < COL:
                        tmp += dp[i - s][j - t] * inv_PQ
                        tmp %= MOD
            dp[i][j] = tmp
print(dp[-1][-1])