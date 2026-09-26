H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

res = 0
tmp = [-1, 0] # end_h, cnt
prv_tmp = None

prv = [False] * W
for w in range(W - 1):
    if A[0][w] == A[0][w + 1]:
        prv[w] = True
        prv[w + 1] = True

for h in range(1, H):
    nxt = [False] * W
    fixed = False
    # 前の行の孤立マスを拾う
    for w in range(W):
        if prv[w] == True:
            continue
        if fixed:
            if A[h - 1][w] != A[h][w]:
                print(-1)
                exit()
            else:
                nxt[w] = True
        else:
            fixed = True
            if A[h - 1][w] != A[h][w]:
                tmp[1] += 1
                for w in range(W):
                    A[h][w] = 1 - A[h][w]

    # 今の行内の隣接マスを処理
    for w in range(W - 1):
        if A[h][w] == A[h][w + 1]:
            nxt[w] = True
            nxt[w + 1] = True

    for w in range(W):
        if A[h][w] == A[h - 1][w]:
            nxt[w] = True

    all_pair = True
    for w in range(W):
        if nxt[w] == False:
            all_pair = False
    if all_pair:
        # print(tmp, h)
        res += min(tmp[1], h - tmp[0] - tmp[1])
        prv_tmp = tmp
        tmp = [h, 0]
    prv = nxt

# print(tmp)
# print(res)

if tmp[0] == H - 2 and not fixed:
    for w in range(W):
        if w < W - 1 and A[H-1][w] == A[H-1][w+1]:
            continue
        elif w > 0 and A[H-1][w] == A[H-1][w-1]:
            continue
        elif 1 - A[H-1][w] == A[H-2][w]:
            fixed = True
            continue
        print(-1)
        exit()
    if fixed:
        prv_block_cnt = min(prv_tmp[1], tmp[0] - prv_tmp[0] - prv_tmp[1])
        other_choice = max(prv_tmp[1], tmp[0] - prv_tmp[0] - prv_tmp[1])
        res -= prv_block_cnt
        print(min(res + prv_block_cnt + 1, res + other_choice))
    else:
        print(res)
elif tmp[0] != H - 1:
    print(-1)
else:
    print(res)
