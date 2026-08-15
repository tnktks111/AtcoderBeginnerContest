N, W = map(int, input().split())
A = list(map(int, input().split()))
res = set([A[i] for i in range(N) if A[i] <= W])
for i in range(N - 1):
    for j in range(i + 1, N):
        if (s := A[i] + A[j]) <= W:
            res.add(s)
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if (s := A[i] + A[j] + A[k]) <= W:
                res.add(s)
print(len(res))
