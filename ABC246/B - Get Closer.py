import math
A, B = map(int, input().split())
dist = math.sqrt(A ** 2 + B ** 2)
res = [0, 0]
res[0] = A / dist
res[1] = B / dist
print(*res)