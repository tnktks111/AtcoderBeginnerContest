N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
INF = float("inf")

# 0->max X, min Y
# 1->max X
# 2->min Y
# 3->Y+1~X-1

dp = [[0, 0, 0, 0] for _ in range(N + 1)]

for i in range(N):
    if A[i] > X or A[i] < Y:
        continue
    elif A[i] == X:
        dp[i+1][0] = dp[i][0] + dp[i][2]
        dp[i+1][1] = dp[i][1] + dp[i][3] + 1
    elif A[i] == Y:
        dp[i+1][0] = dp[i][0] + dp[i][1]
        dp[i+1][2] = dp[i][2] + dp[i][3] + 1
    else:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1]
        dp[i+1][2] = dp[i][2]
        dp[i+1][3] = dp[i][3] + 1

# print(dp)

res = 0
if X != Y:
    for i in range(N + 1):
        res += dp[i][0]
else:
    for i in range(N + 1):
        res += dp[i][1]

print(res)