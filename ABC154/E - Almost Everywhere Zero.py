
"""
NがD桁
dp[d][i][isIdenticalWithN][haveNonZero]...d桁まで決まっていて、0でない個数がi個で、決定済み桁がNに一致か、0以外が出たか

dpの値がA
if not haveNonZero:
    dp[d + 1][i][False][False] += A
    dp[d + 1][i + 1][False][True] += 9 * A  # 1~9を追加

else:
    if isIdenticalWithN
        if Nのd+1桁目が0:
            dp[d + 1][i][True][True] += A
        else:
            Nのd+1桁目がkだとして、
            dp[d + 1][i][False][True] += A
            dp[d + 1][i + 1][False][True] += A * (k - 1)
            dp[d + 1][i + 1][True][True] += A
    else:
        dp[d + 1][i][False][True] += A
        dp[d + 1][i + 1][False][True] += A * 9
"""

from collections import defaultdict

N = int(input())
K = int(input())

list_N = list(map(int, list(str(N))))
D = len(str(N))

dp = {(1, True, True): 1, (0, False, False): 1}
if list_N[0] != 1:
    dp[(1, False, True)] = list_N[0] - 1

for d in range(2, D + 1):
    next_dp = defaultdict(int)
    for (i, isIdenticalWithN, haveNonZero), val in dp.items():
        if not haveNonZero:
            next_dp[(i, False, False)] += val
            next_dp[(i + 1, False, True)] += val * 9
        else:
            if isIdenticalWithN:
                if list_N[d - 1] == 0:
                    next_dp[(i, True, True)] += val
                else:
                    k = list_N[d - 1]
                    next_dp[(i, False, True)] += val
                    if i + 1 <= K:
                        next_dp[(i + 1, False, True)] += val * (k - 1)
                        next_dp[(i + 1, True, True)] += val
            else:
                next_dp[(i, False, True)] += val
                if i + 1 <= K:
                    next_dp[(i + 1, False, True)] += val * 9
    dp = next_dp

res = 0
res += dp.get((K, True, True), 0)
res += dp.get((K, False, True), 0)
print(res)


# from collections import defaultdict

# N = input()
# K = int(input())

# # dp[(非ゼロ桁数, Nとここまで一致しているか)] = 個数
# dp = {(0, True): 1}

# for nd_char in N:
#     nd = int(nd_char)
#     next_dp = defaultdict(int)

#     for (cnt, tight), val in dp.items():
#         upper = nd if tight else 9

#         for x in range(upper + 1):
#             next_cnt = cnt + (x != 0)

#             if next_cnt > K:
#                 continue

#             next_tight = tight and (x == nd)
#             next_dp[(next_cnt, next_tight)] += val

#     dp = next_dp

# print(dp.get((K, False), 0) + dp.get((K, True), 0))


# from functools import cache

# N = input()
# K = int(input())
# D = len(N)

# @cache
# def dfs(d: int, cnt: int, tight: bool) -> int:
#     """
#     上から d 桁を決めた状態。

#     cnt:
#         ここまでに使った非ゼロ桁の個数

#     tight:
#         ここまで N と完全に一致しているか
#         True なら次の桁は N[d] 以下
#         False なら次の桁は 0～9
#     """
#     if cnt > K:
#         return 0

#     if d == D:
#         return int(cnt == K)

#     limit = int(N[d]) if tight else 9

#     res = 0

#     for x in range(limit + 1):
#         next_cnt = cnt + (x != 0)
#         next_tight = tight and (x == limit)

#         res += dfs(d + 1, next_cnt, next_tight)

#     return res

# print(dfs(0, 0, True))