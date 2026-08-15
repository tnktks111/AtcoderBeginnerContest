from collections import defaultdict
from functools import cache

N, L = map(int, input().split())
A = list(map(int, input().split()))

# A[i]に対し 2i と 2i+1 がペア

dp = defaultdict(lambda: -1)

def pair(n:int):
    return n + 1 if n % 2 == 0 else n - 1


"""
既知以外のiをひく
    ①iのpairの位置を知っている→それをひく
    ②iのpair位置を知らない
        jをひく
        2-1. たまたまiのpairを引く→lifeは減らない, 得点
        2-2. そうでない lifeは減る
            jのpairの位置を知っている→jのpairを引ける(lifeがあるなら)ので得点として加算する
            jのpairの位置を知らない→そのまま
"""

# def dfs(know:int, life:int, unknown_cnt:int):
#     if life == 0:
#         return 0
#     if dp[(know, life)] != -1:
#          return dp[(know, life)]

#     res = 0
#     for i in range(2 * N):
#         if (1 << i) & know:
#             continue
#         know |= (1 << i)
#         i_pair = pair(i)
#         num = A[i // 2]

#         if know & (1 << i_pair):
#             res += (num + dfs(know, life, unknown_cnt - 1)) / (unknown_cnt)
#         else:
#             for j in range(2 * N):
#                 if (1 << j) & know:
#                     continue
#                 know |= (1 << j)
#                 if j == i_pair:
#                     res += (num + dfs(know, life, unknown_cnt - 2)) / (unknown_cnt * (unknown_cnt - 1))
#                 else:
#                     if life == 1:
#                         know ^= (1 << j)
#                         continue
#                     else:
#                         j_pair = pair(j)
#                         if know & (1 << j_pair):
#                             res += (A[j // 2] + dfs(know, life - 1, unknown_cnt - 2)) / (unknown_cnt * (unknown_cnt - 1))
#                         else:
#                             res += (dfs(know, life - 1, unknown_cnt - 2)) / (unknown_cnt * (unknown_cnt - 1))
#                 know ^= (1 << j)
#         know ^= (1 << i)

#     dp[(know, life)] = res
#     return res

# print(dfs(0, L, 2 * N))
# for k, v in dp.items():
#     print(f"({bin(k[0])[2:]} = {k[0]}, {k[1]}), {v}")

def key2tuple(key:int):
    tmp, know = divmod(key, 1000)
    life, unknown = divmod(tmp, 1000)
    return (life, unknown, know)

def tuple2key(life: int, unknown:int, know:int):
    return 1000000 * life + 1000 * unknown + know

# unknown...未知の枚数, know...既知の片割れ
dp = defaultdict(lambda : -1)
# key = 1000000 * life + 1000 * unknown + know
def dfs(key:int):
    if dp[key] != -1:
        return dp[key]
    life, unknown, know = key2tuple(key)
    if life == 0:
        return 0
    if unknown <= 1:
        return unknown

    res = 0
    # 1枚目のペアが既知
    if know > 0:
        res += (know / unknown) * (1 + dfs(tuple2key(life, unknown - 1, know - 1)))
    # 1枚目のペアが未知だが、2枚目と1枚目がペア
    res += (1 - know / unknown) * (1 / (unknown - 1)) * (1 + dfs(tuple2key(life, unknown - 2, know)))
    if life >= 2:
        # 1枚目のペアが未知、2枚目のペアが既知
        res += (1 - know / unknown) * (know / (unknown - 1)) * (1 + dfs(tuple2key(life - 1, unknown - 2, know)))
        # 1枚目のペアが未知、2枚目のペアが未知
        res += (1 - know / unknown) * (1 - (know + 1) / (unknown - 1)) * (dfs(tuple2key(life - 1, unknown - 2, know + 2)))
    dp[key] = res
    return res

print(sum(A) / N * dfs(tuple2key(L, 2 * N, 0)))
# for k, v in dp.items():
#     print(k, v)