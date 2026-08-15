H, W = map(int, input().split())
res = [0] * min(H, W)
board = [list(input()) for _ in range(H)]

seen = set()

def dfs(r, c, diag, R, C):
    if (r, c) in seen:
        return diag
    if r < 0 or r >= R or c < 0 or c >= C or board[r][c] == ".":
        return diag
    seen.add((r, c))
    return (dfs(r + 1, c + 1, diag + 1, R, C))

for h in range(H):
    for w in range(W):
        if board[h][w] == ".":
            continue
        if (h, w) in seen:
            continue
        size = dfs(h, w, 0, H, W) // 2
        if size == 0:
            continue
        res[size - 1] += 1

print(*res)