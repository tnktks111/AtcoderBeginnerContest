from collections import deque

H, W = map(int, input().split())
INF = float("inf")
DIR_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = [list(input()) for _ in range(H)]

watchers = []
start, goal = None, None

def in_board(h:int, w:int):
    return 0 <= h < H and 0 <= w < W

for h in range(H):
    for w in range(W):
        match board[h][w]:
            case ">":
                watchers.append(((h, w), (0, 1)))
            case "v":
                watchers.append(((h, w), (1, 0)))
            case "<":
                watchers.append(((h, w), (0, -1)))
            case "^":
                watchers.append(((h, w), (-1, 0)))
            case "S":
                start = (h, w)
            case "G":
                goal = (h, w)

for (h, w), (dh, dw) in watchers:
    ch, cw = h + dh, w + dw
    while in_board(ch, cw) and board[ch][cw] in {"!", "."}:
        board[ch][cw] = "!"
        ch += dh
        cw += dw

dists = [[INF] * W for _ in range(H)]

q = deque([(0, start)])
dists[start[0]][start[1]] = 0

while q:
    d, (h, w) = q.popleft()
    for dh, dw in DIR_4:
        nh, nw = h + dh, w + dw
        if not in_board(nh, nw):
            continue
        if board[nh][nw] in {"!", "#", ">", "v", "<", "^"}:
            continue
        if dists[nh][nw] <= d + 1:
            continue
        dists[nh][nw] = d + 1
        q.append((d + 1, (nh, nw)))

res = dists[goal[0]][goal[1]]

print(res if res != INF else -1)