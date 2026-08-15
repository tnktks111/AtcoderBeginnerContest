N = int(input())
dp = [0] * 101
for i in range(N):
    tmp = 0
    for j in range(1, 7):
        if dp[i] < j:
            tmp += j
        else:
            tmp += dp[i]
    dp[i + 1] = tmp / 6
print(dp[N])