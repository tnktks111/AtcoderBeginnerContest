from collections import deque
N = int(input())
query = list(tuple(map(int, input().split())) for _ in range(N))
q = deque(query)

t, x, a = q.pop()
finish = False
dp = [[0] * 5 for _ in range(t + 1)]
for i in range(len(dp) - 1, -1, -1):
    if i != len(dp) - 1:
        for j in range(5):
            if j == 0:
                dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
            elif j == 4:
                dp[i][j] = max(dp[i+1][j], dp[i+1][j-1])
            else:
                dp[i][j] = max(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])
    if not finish and i == t:
        dp[i][x] += a
        if q:
            t, x, a = q.pop()
        else:
            finish = True
print(dp[0][0])