N, X = map(int, input().split())
elements = [list(map(int, input().split())) for _ in range(N)]
res = [0]
def dfs(idx, cur):
    if idx == N:
        if cur == X:
            res[0] += 1
        return
    if cur > X:
        return
    for i in range(1, elements[idx][0] + 1):
        dfs(idx + 1, cur * elements[idx][i])

dfs(0, 1)
print(res[0])


#問題文誤読、DPでやろうとしたけどメモリ的に無理
# N, X = map(int, input().split())
# elements = [list(map(int, input().split())) for _ in range(N)]
# if X > (10 ** 5):
#     print(0)
#     exit()
# dp = [[0] * (X + 1) for _ in range(N + 1)]
# dp[0][X] = 1
# for i in range(1, N + 1):
#     n = elements[i - 1][0]
#     for j in range(X + 1):
#         if dp[i - 1][j]:
#             for k in range(1, n + 1):
#                 div = j // elements[i - 1][k]
#                 mod = j % elements[i - 1][k]
#                 if not mod:
#                     dp[i][div] += dp[i - 1][j]
# print(dp[N][1])
