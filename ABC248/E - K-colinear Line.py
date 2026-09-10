import math
from collections import defaultdict

def calc_line_hash(p1:tuple[int, int], p2:tuple[int, int]):
    if p1[0] > p2[0]:
        p1, p2 = p2, p1
    y_corr = p2[0] - p1[0]
    x_corr = -(p2[1] - p1[1])
    const = p2[0] * p1[1] - p1[0] * p2[1]
    if y_corr == 0 and x_corr < 0:
        x_corr *= -1
        const *= -1
    m = math.gcd(y_corr, x_corr, const)
    return (y_corr // m, x_corr // m, const // m)

N, K = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]

if K == 1:
    print("Infinity")
    exit()

line2points = defaultdict(lambda : set())
for i in range(N - 1):
    for j in range(i + 1, N):
        h = calc_line_hash(points[i], points[j])
        line2points[h].add(i)
        line2points[h].add(j)

res = 0
for k, v in line2points.items():
    # print(k, v)
    if len(v) >= K:
        res += 1


print(res)
