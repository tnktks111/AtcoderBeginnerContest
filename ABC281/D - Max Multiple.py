N, K, D = map(int, input().split())
A = list(map(int, input().split()))

DP = [[-float("inf")] * D for _ in range(K + 1)]
DP[0][0] = 0
for i in range(N):
    for k in range(i, -1, -1):
        if k >= K:
            continue
        for d in range(D):
            if DP[k][d] >= 0:
                DP[k + 1][(d + A[i]) % D] = max(DP[k + 1][(d + A[i]) % D], DP[k][d] + A[i])
DP[K][0] = max(DP[K][0], -1)
print(DP[K][0])
