N = int(input())

def is_lower_than_n(a:int, d:int, l:int, n:int):
    res = 1
    for i in range(l):
        res *= (a + i * d)
    return res <= n

res = 0
for l in range(3, 21):
    for a in range(1, N):
        for d in range(1, N):
            if is_lower_than_n(a, d, l, N):
                res += 1

print(res)