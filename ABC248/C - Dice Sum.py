mod = 998244353
N, M, K = map(int, input().split())
DP = [[0] * K for _ in range(N)]
for i in range(M):
    DP[0][i] = 1
for i in range(1, N):
    prefix_sum = [0] * (K+1)
    for k in range(K):
        prefix_sum[k+1] = (prefix_sum[k] + DP[i - 1][k]) % mod
    for j in range(K):
        DP[i][j] = (prefix_sum[j] - prefix_sum[max(0, j - M)] + mod) % mod
print(sum(DP[N - 1]) % mod)