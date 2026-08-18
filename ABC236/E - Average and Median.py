N = int(input())
A = list(map(int, input().split()))

def can_have_avg_k(k:int):
    delta = [a - k for a in A]
    dp = [[0, 0] for _ in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][0]) + delta[i - 1]
        dp[i][1] = dp[i - 1][0]
    return True if dp[N][0] >= 0 or dp[N][1] >= 0 else False

def can_have_median_k(k:int):
    delta = [1 if a >= k else -1 for a in A]
    dp = [[0, 0] for _ in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][0]) + delta[i - 1]
        dp[i][1] = dp[i - 1][0]
    return True if dp[i][0] > 0 or dp[i][1] > 0 else False

l = 0.0
r = 10 ** 9
while r - l > 0.0001:
    m = (l + r) / 2
    if can_have_avg_k(m):
        l = m
    else:
        r = m

print(l)

l = 0
r = 10 ** 9 + 1
while r - l > 1:
    # print(l, r)
    m = (l + r) // 2
    if can_have_median_k(m):
        l = m
    else:
        r = m
print(l)
