H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

res = [0]
def dfs(h, w, seen:set, H, W) -> None:
    if h == H or w == W:
        return
    num = A[h][w]
    if num in seen:
        return
    seen.add(num)
    if (h == H - 1 and w == W - 1):
        res[0] += 1
    dfs(h + 1, w, seen.copy(), H, W)
    dfs(h, w + 1, seen.copy(), H, W)

dfs(0, 0, set(), H, W)
print(res[0])