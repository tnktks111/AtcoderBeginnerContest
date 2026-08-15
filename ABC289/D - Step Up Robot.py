N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

dp = [0] * (X + 1)
dp[0] = 1
for j in range(M):
    dp[B[j]] = -1

for i in range(X):
    if dp[i] == 1:
        for j in A:
            if i + j <= X and dp[i + j] != -1:
                dp[i + j] = 1
print("Yes" if dp[X] == 1 else "No")