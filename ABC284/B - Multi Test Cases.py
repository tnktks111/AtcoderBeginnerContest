from collections import Counter
T = int(input())
res = []
for _ in range(T):
    N = int(input())
    A = list(map(lambda x: x % 2, map(int, input().split())))
    c = Counter(A)
    res.append(c[1])
print(*res, sep="\n")