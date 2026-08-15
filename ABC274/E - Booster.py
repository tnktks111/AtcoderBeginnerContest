import sys
import math
sys.setrecursionlimit(2 * 10**5)
INF = float("inf")
N, M = map(int, input().split())

#(Nのbit)(原点のbit)(Mのbit)
M_mask = (1 << M) - 1
N_one_mask = ((1 << (N + 1)) - 1) << M
start_mask = 1 << M
dist = [[0] * (N + M + 1) for _ in range(N + M + 1)]
coords = []
for _ in range(N + M):
    x, y = map(int, input().split())
    coords.append((x, y))

coords = coords[N:] + [(0, 0)] + coords[:N]
for i in range(M + N + 1):
    for j in range(M + N + 1):
        dist[i][j] = math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)

dp = [[-1.0] * (M + N + 1) for _ in range(1 << (M + N + 1))]

def rec(S:int, v:int):
    if S == 0:
        if v == M:
            return 0
        else:
            return INF 

    if not (S & (1 << v)):
        return INF

    if dp[S][v] != -1.0:
        return dp[S][v]

    ret = INF
    for u in range(M + N + 1):
        S_prev = S ^ (1 << v)
        cost = rec(S_prev, u)
        if cost != INF:
            speed = 2 ** ((S_prev & M_mask).bit_count())
            ret = min(ret, cost + dist[u][v] / speed)
    dp[S][v] = ret
    return ret

res = INF

for i in range(N_one_mask, 1 << (M + N + 1)):
    res = min(res, rec(i, M))
# print(dp)
print(res)
