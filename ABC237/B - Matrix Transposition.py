H, W = map(int, input().split())
Matrix = [[0] * H for _ in range(W)]
for i in range(H):
    A_i = list(map(int, input().split()))
    for j in range(W):
        Matrix[j][i] = A_i[j]
for i in range(W):
    print(*Matrix[i])
