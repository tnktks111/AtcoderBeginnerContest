import sys
sys.setrecursionlimit(10 ** 6)

from collections import defaultdict

H, W, N = map(int, input().split())

def coordinate2idx(r:int, c:int):
    return r * W + c
def idx2coordinate(idx:int):
    return tuple(divmod(idx, W))

non_zeros = []
non_zeros_sorted = []
rows = [[] for _ in range(H)]
cols = [[] for _ in range(W)]

rows_nxt_num = [dict() for _ in range(H)]
cols_nxt_num = [dict() for _ in range(W)]
rows_max = [defaultdict(int) for _ in range(H)]
cols_max = [defaultdict(int) for _ in range(W)]

coordinate2num = dict()
for _ in range(N):
    r, c, a = map(int, input().split())
    r -= 1
    c -= 1
    non_zeros.append((r, c))
    non_zeros_sorted.append((a, r, c))
    rows[r].append(a)
    cols[c].append(a)
    coordinate2num[coordinate2idx(r, c)] = a

non_zeros_set = set([coordinate2idx(r, c) for r, c in non_zeros])

for r in range(H):
    rows[r].sort()
    for i in range(len(rows[r])):
        if i != len(rows[r]) - 1:
            rows_nxt_num[r][rows[r][i]] = rows[r][i + 1]
        else:
            rows_nxt_num[r][rows[r][i]] = -1

for c in range(W):
    cols[c].sort()
    for i in range(len(cols[c])):
        if i != len(cols[c]) - 1:
            cols_nxt_num[c][cols[c][i]] = cols[c][i + 1]
        else:
            cols_nxt_num[c][cols[c][i]] = -1

dp = defaultdict(lambda: -1)

# 同じ行・列の次の数字以上の最大値がわかればok
# rows_max[r][a] -> a以上のマスの最大値

def dfs(idx: int):
    if idx not in non_zeros_set:
        return 0
    if dp[idx] != -1:
        return dp[idx]

    r, c = idx2coordinate(idx)
    a = coordinate2num[idx]

    res = 0

    if rows_nxt_num[r][a] != -1:
        res = max(res, 1 + rows_max[r][rows_nxt_num[r][a]])
    # start_idx = rows_start_idx[r][a]
    # if start_idx != len(rows[r]):
    #     for i in range(start_idx, len(rows[r])):
    #         nr, nc = r, rows[r][i][1]
    #         res = max(res, 1 + dfs(coordinate2idx(nr, nc)))

    if cols_nxt_num[c][a] != -1:
        res = max(res, 1 + cols_max[c][cols_nxt_num[c][a]])

    # start_idx = cols_start_idx[c][a]
    # if start_idx != len(cols[c]):
    #     for i in range(start_idx, len(cols[c])):
    #         nr, nc = cols[c][i][1], c
    #         res = max(res, 1 + dfs(coordinate2idx(nr, nc)))

    dp[idx] = res
    rows_max[r][a] = max(rows_max[r][a], res)
    cols_max[c][a] = max(cols_max[c][a], res)
    return res

non_zeros_sorted.sort(reverse=True)
for a, r, c in non_zeros_sorted:
    dfs(coordinate2idx(r, c))

for r, c in non_zeros:
    print(dp[coordinate2idx(r, c)])