import math
N, M = map(int, input().split())

if N * N < M:
    print(-1)
    exit()

res = float("inf")
for a in range(1, math.ceil(math.sqrt(M)) + 1):
    b = math.ceil(M / a)
    if b > N:
        continue
    res = min(a * b, res)

print(res)