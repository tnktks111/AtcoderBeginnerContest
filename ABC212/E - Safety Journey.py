N, M, K = map(int, input().split())
MOD = 998244353

not_adj = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    not_adj[u].append(v)
    not_adj[v].append(u)

dp = [[0] * N for _ in range(K + 1)]
dp[0][0] = 1
prev_sum = 1

for k in range(1, K + 1):
    cur_sum = 0
    for i in range(N):
        tmp = prev_sum
        tmp = (tmp - dp[k - 1][i]) % MOD
        for not_nei in not_adj[i]:
            tmp = (tmp - dp[k - 1][not_nei]) % MOD
        dp[k][i] = tmp
        cur_sum = (cur_sum + tmp) % MOD
    prev_sum = cur_sum

# print(*dp, sep="\n")
print(dp[K][0])