from collections import deque

H, W = map(int, input().split())
DIR_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = float("inf")
board = [input() for _ in range(H)]

def on_board(r:int, c:int):
    return 0 <= r < H and 0 <= c < W

start = None

for h in range(H):
    for w in range(W):
        if board[h][w] == "S":
            start = (h, w)

assert start is not None
dist = [[[-1] * 4 for _ in range(W)] for _ in range(H)]
dist[start[0]][start[1]] = [0, 0, 0, 0]

for i, dir in enumerate(DIR_4):
    first = (start[0] + dir[0], start[1] + dir[1])
    if not on_board(first[0], first[1]) or board[first[0]][first[1]] == "#":
        continue
    dist[first[0]][first[1]][i] = 1
    q = deque()
    q.append((1, first))
    while q:
        d, (r, c) = q.popleft()
        for dr, dc in DIR_4:
            nr, nc = r + dr, c + dc
            if not on_board(nr, nc):
                continue
            if board[nr][nc] == "#":
                continue
            if dist[nr][nc][i] != -1 and dist[nr][nc][i] <= d + 1:
                continue
            dist[nr][nc][i] = d + 1
            q.append((d + 1, (nr, nc)))

def calc_dist(r:int, c:int):
    tmp = sorted(dist[r][c], reverse=True)
    if tmp[1] == -1:
        return -1
    else:
        return tmp[0] + tmp[1]

# for r in range(H):
#     print(dist[r])

for r in range(H):
    for c in range(W):
        if calc_dist(r, c) >= 4:
            print("Yes")
            exit()
print("No")