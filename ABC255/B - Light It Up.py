import math
N, K = map(int, input().split())
A = set(map(int, input().split()))
lights = []
points = []
res = 0

def dist(a:tuple, b:tuple) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

for i in range(1, N + 1):
    point = tuple(map(int, input().split()))
    if i in A:
        lights.append(point)
    else:
        points.append(point)

for point in points:
    cur = float("inf")
    for light in lights:
        cur = min(cur, dist(point, light))
    res = max(res, cur)

print(math.sqrt(res))