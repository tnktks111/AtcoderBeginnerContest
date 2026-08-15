H, W = map(int, input().split())
S = [input() for _ in range(H)]
points = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "o":
            points.append((i, j))
print(abs(points[0][0] - points[1][0]) + abs(points[0][1] - points[1][1]))