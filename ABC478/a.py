N, M = map(int, input().split())

p, q = divmod(M, N)

for _ in range(q):
    print(p + 1)
for _ in range(N - q):
    print(p)