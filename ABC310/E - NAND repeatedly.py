N = int(input())

S = input()

dp = [[0] * (N + 1) for _ in range(2)]

for i in range(1, N + 1):
    if S[i - 1] == "0":
        dp[0][i] = 1
        dp[1][i] = dp[0][i - 1] + dp[1][i - 1]
    else:
        dp[0][i] = dp[1][i - 1]
        dp[1][i] = dp[0][i - 1] + 1

# print(dp)
print(sum(dp[1]))