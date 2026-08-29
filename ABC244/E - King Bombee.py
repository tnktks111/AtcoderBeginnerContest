N, M, K, S, T, X = map(int, input().split())
MOD = 998244353

S -= 1
T -= 1
X -= 1

adj = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    adj[u].append(v)
    adj[v].append(u)

# 0 -> 偶数回、1 -> 奇数回
dp = [[0] * N for _ in range(2)]
dp[0][S] = 1

for _ in range(K):
    next_dp = [[0] * N for _ in range(2)]
    for i in range(N):
        if i == X:
            for nei in adj[i]:
                next_dp[0][i] += dp[1][nei]
                next_dp[0][i] %= MOD
                next_dp[1][i] += dp[0][nei]
                next_dp[1][i] %= MOD
        else:
            for nei in adj[i]:
                next_dp[0][i] += dp[0][nei]
                next_dp[0][i] %= MOD
                next_dp[1][i] += dp[1][nei]
                next_dp[1][i] %= MOD
    dp = next_dp

print(dp[0][T])