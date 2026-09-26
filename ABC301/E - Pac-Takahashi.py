from collections import deque

H, W, T = map(int, input().split())
DIR_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = float("inf")

def in_board(h:int, w:int):
    return 0 <= h < H and 0 <= w < W

# dist[h][w][c]...c個のお菓子を取得するのに必要な最小手数
dist = [[[INF] * 19 for _ in range(W)] for _ in range(H)]
board = [input() for _ in range(H)]

start, goal = None, None

for h in range(H):
    for w in range(W):
        if board[h][w] == "S":
            start = (h, w)
        if board[h][w] == "G":
            goal = (h, w)

q = deque()

q.append((0, 0, start[0], start[1]))
dist[start[0]][start[1]][0] = 0

while q:
    d, candy_cnt, h, w = q.popleft()
    for dh, dw in DIR_4:
        nh, nw = h + dh, w + dw

        if not in_board(nh, nw):
            continue
        if board[h][w] == "#":
            continue

        new_candy_cnt = candy_cnt + 1 if board[nh][nw] == "o" else candy_cnt
        new_d = d + 1

        if new_d > T:
            continue

        use = True
        for c in range(new_candy_cnt, 19):
            if dist[nh][nw][c] <= new_d:
                use = False 
                break
        if not use:
            continue

        q.append((new_d, new_candy_cnt, nh, nw))
        dist[nh][nw][new_candy_cnt] = new_d

res = -1
for c in range(19):
    if dist[goal[0]][goal[1]][c] != INF:
        res = c

print(res)