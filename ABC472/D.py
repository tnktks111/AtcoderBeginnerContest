from collections import deque

DIR_4 = [(-1, 0), (1, 0), (0, 1), (0, -1)]
H, W, K = map(int, input().split())
board = [input() for _ in range(H)]

danger_rows = set()
danger_cols = set()

for r in range(H):
    for c in range(W):
        if board[r][c] == "#":
            danger_rows.add(r)
            danger_cols.add(c)

res = set()
stack = []
for r in range(H):
    if r in danger_rows:
        continue
    for c in range(W):
        if c in danger_cols:
            continue
        stack.append((r, c))
        res.add((r, c))

for i in range(K):
    new_stack = []
    for r, c in stack:
        for dr, dc in DIR_4:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < H and 0 <= nc < W):
                continue
            if board[nr][nc] == "#":
                continue
            if (nr, nc) in res:
                continue
            new_stack.append((nr, nc))
            res.add((nr, nc))
    stack = new_stack

print(len(res))