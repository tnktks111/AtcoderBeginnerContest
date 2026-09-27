N, D = map(int, input().split())
X = list(map(int, input().split()))

num2idx = {x: i for i, x in enumerate(X)}
X.sort()

res = []
for i in range(N):
    issen = True
    if i != 0 and X[i] - X[i - 1] < D:
        issen = False
    if i != N - 1 and X[i + 1] - X[i] < D:
        issen = False
    if issen:
        res.append(num2idx[X[i]] + 1)

res.sort()
print(len(res))
print(*res)