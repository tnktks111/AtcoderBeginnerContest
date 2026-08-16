H, W, K = map(int, input().split())
MOD = 998244353
coordinates = tuple(map(lambda x: int(x) - 1, input().split()))
start = (coordinates[0], coordinates[1])
goal = (coordinates[2], coordinates[3])

p = H + W - 2
inv_p = pow(p, MOD - 2, MOD)

type_1 = 1
type_2 = 0
type_3 = 0
type_4 = 0

dp = [1, 0, 0, 0]
for _ in range(K):
    next_dp = [0] * 4
    next_dp[0] = (dp[1] * (H - 1) % MOD + dp[2] * (W - 1) % MOD) % MOD
    next_dp[1] = (dp[0] + dp[1] * (H - 2) % MOD + dp[3] * (W - 1) % MOD) % MOD
    next_dp[2] = (dp[0] + dp[2] * (W - 2) % MOD + dp[3] * (H - 1) % MOD) % MOD
    next_dp[3] = (dp[1] + dp[2] + dp[3] * (H + W - 4) % MOD) % MOD
    dp = next_dp

if goal == start:
    print(dp[0])
elif goal[0] == start[0]:
    print(dp[2])
elif goal[1] == start[1]:
    print(dp[1])
else:
    print(dp[3])