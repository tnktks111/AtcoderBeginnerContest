from copy import deepcopy

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
DIR4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = float("inf")

for bit in range((1 << H)):
    tmp = deepcopy(A)
    cnt = 0
    for h in range(H):
        if bit & (1 << h):
            cnt += 1
            for w in range(W):
                tmp[h][w] = 1 - tmp[h][w]

    isolation_found = False
    for h in range(H):
        for w in range(W):
            isolated = True
            for dh, dw in DIR4:
                nh, nw = h + dh, w + dw
                if not (0 <= nh < H and 0 <= nw < W):
                    continue
                if tmp[nh][nw] == tmp[h][w]:
                    isolated = False
            if isolated:
                isolation_found = True
    if not isolation_found:
        res = min(res, cnt)

print(res if res != float("inf") else -1)


