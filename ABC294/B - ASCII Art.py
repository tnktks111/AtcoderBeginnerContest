H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
for h in range(H):
    for w in range(W):
        A[h][w] = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"[A[h][w]]

for h in range(H):
    print("".join(A[h]))
