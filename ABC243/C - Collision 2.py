from collections import defaultdict
N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]
S = input()
ys = defaultdict(lambda: [-float("inf"), float("inf")])
for i in range(N):
    if S[i] == "L":
        ys[XY[i][1]][0] = max(ys[XY[i][1]][0], XY[i][0])
    else:
        ys[XY[i][1]][1] = min(ys[XY[i][1]][1], XY[i][0])
for y in ys:
    if ys[y][0] >= ys[y][1]:
        print("Yes")
        exit()
print("No")