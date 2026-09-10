N = int(input())
A = list(map(int, input().split()))
INF = float("inf")

# def debug():
#     for i in range((1 << N)):
#         tmp = 0
#         prev_zero = False
#         out_condition = False
#         for j in range(N):
#             if out_condition:
#                 break
#             if (1 << j) & i:
#                 tmp += A[j]
#                 prev_zero = False
#             else:
#                 if prev_zero:
#                     out_condition = True
#                 prev_zero = True
#         if tmp == 426:
#             print(bin(i)[::-1])

# debug()

res = INF
# 0-1辺を使う場合
dp = [[INF] * N for _ in range(2)]
dp[0][0] = A[0]
for i in range(1, N):
    dp[0][i] = min(dp[0][i-1], dp[1][i-1]) + A[i]
    dp[1][i] = dp[0][i-1]
res = min(res, dp[0][-1], dp[1][-1])

# print(dp[0])
# print(dp[1])

# (N-1)-0辺を使う場合
dp = [[INF] * N for _ in range(2)]
dp[0][0] = A[-1]
for i in range(1, N):
    dp[0][i] = min(dp[0][i-1], dp[1][i-1]) + A[i-1]
    dp[1][i] = dp[0][i-1]
res = min(res, dp[0][-1], dp[1][-1])

# print(dp[0])
# print(dp[1])

print(res)