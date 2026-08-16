import math

N = int(input())

res = 0
cur = N
while cur != 0:
    a = math.floor(N / cur)
    sup = math.floor(N / a)
    inf = math.floor(N / (a + 1) + 1)
    res += a * (sup - inf + 1)
    cur = inf - 1

print(res)