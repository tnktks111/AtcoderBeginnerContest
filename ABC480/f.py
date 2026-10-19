N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * (1 << N)
T = sum(A) // M

for mask in range(1 << N):
    cur_mod = 0
    for i in range(N):
        if (1 << i) & mask:
            cur_mod += A[i]
            cur_mod %= T

    for i in range(N):
        if (1 << i) & mask:
            continue
        nxt = mask | (1 << i)
        if (cur_mod + A[i]) % T == 0:
            dp[nxt] = max(dp[nxt], dp[mask] + 1)
        else:
            dp[nxt] = max(dp[nxt], dp[mask])

print(M - dp[-1])