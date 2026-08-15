N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * (N + 1)

def nibutan_left(x:int):
    ok = -1
    ng = len(A)
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if A[mid] <= x:
            ok = mid
        else:
            ng = mid
    return ok

for i in range(1, N + 1):
    dp[i] = max([i - dp[i - A[j]] for j in range(nibutan_left(i) + 1)])

print(dp[-1])