from collections import deque

H, W, T = map(int, input().split())
DIR_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = float("inf")

def in_board(h:int, w:int):
    return 0 <= h < H and 0 <= w < W

board = [input() for _ in range(H)]

start, goal = None, None
check_points = []

for h in range(H):
    for w in range(W):
        match board[h][w]:
            case "S":
                start = (h, w)
            case "G":
                goal = (h, w)
            case "o":
                check_points.append((h, w))

check_points.insert(0, start)
check_points.append(goal)

dists = [[[INF] * W for _ in range(H)] for _ in range(len(check_points))]

for i, begin in enumerate(check_points):
    stack = [begin]
    dists[i][begin[0]][begin[1]] = 0
    dist = 1
    while stack:
        nxt_stack = []
        for u in stack:
            ur, uc = u
            for dr, dc in DIR_4:
                nr, nc = ur + dr, uc + dc
                if not in_board(nr, nc):
                    continue
                if board[nr][nc] == "#":
                    continue
                if dists[i][nr][nc] != INF:
                    continue
                dists[i][nr][nc] = dist
                nxt_stack.append((nr, nc))
        stack = nxt_stack
        dist += 1

check_point_dists = [[INF] * len(check_points) for _ in range(len(check_points))]

for i, u in enumerate(check_points):
    for j, v in enumerate(check_points):
        check_point_dists[i][j] = dists[i][v[0]][v[1]]
# print(*check_point_dists, sep="\n")

snack_cnts = len(check_points) - 2

dp = [[INF] * snack_cnts for _ in range(1 << snack_cnts)]
for i in range(snack_cnts):
    dp[(1 << i)][i] = check_point_dists[0][i + 1]

for bit in range(1 << snack_cnts):
    for u in range(snack_cnts):
        if (1 << u) & bit == 0:
            continue
        if dp[bit][u] > T:
            continue
        for v in range(snack_cnts):
            nxt_bit = bit | (1 << v)
            dp[nxt_bit][v] = min(check_point_dists[1 + u][1 + v] + dp[bit][u], dp[nxt_bit][v])

# print(*dp, sep="\n")

res = 0 if check_point_dists[0][-1] <= T else -1
for bit in range(1 << snack_cnts):
    for u in range(snack_cnts):
        if dp[bit][u] + check_point_dists[1 + u][-1] <= T:
            res = max(res, bit.bit_count())

print(res)