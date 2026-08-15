from collections import deque

H, W = map(int, input().split())
INF = float("inf")
DIR4 = [(-1, 0), (1, 0), (0, 1), (0, -1)]
PUNCH = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def onboard(r:int, c:int):
    return 0 <= r < H and 0 <= c < W

board = [input() for _ in range(H)]

start = (0, 0)
goal = (H - 1, W - 1)

q = deque([(0, start)])
dist = [[INF] * W for _ in range(H)]

while q:
    d, (r, c) = q.popleft()
    if dist[r][c] <= d:
        continue
    dist[r][c] = d
    if (r, c) == goal:
        break
    for dr, dc in DIR4:
        nr, nc = r + dr, c + dc
        if not onboard(nr, nc):
            continue
        if board[nr][nc] == ".":
            if dist[nr][nc] <= d:
                continue
            q.appendleft((d, (nr, nc)))
        else:
            for ddr, ddc in PUNCH:
                nnr, nnc = nr + ddr, nc + ddc
                if not onboard(nnr, nnc):
                    continue
                if board[nnr][nnc] == ".":
                    continue
                if dist[nnr][nnc] <= d + 1:
                    continue
                q.append((d + 1, (nnr, nnc)))

print(dist[H - 1][W - 1])