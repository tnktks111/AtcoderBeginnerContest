import math
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
curMax = 0
for i in range(N):
    for j in range(i + 1, N):
        curMax = max(curMax, (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
print(math.sqrt(curMax))