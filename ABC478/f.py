from sortedcontainers import SortedList

N = int(input())
Q = list(map(lambda x: int(x) - 1, input().split()))
MOD = 998244353

seen = SortedList([0])
num2idx = [0] * N
for i in range(N):
    num2idx[Q[i]] = i

dp = [1] * N
num2times = [1] * N

for i in range(N - 1, 0, -1):
    left_idx = seen.bisect_left(num2idx[i]) - 1
    if left_idx == -1:
        num2times[i] = num2idx[i]
    else:
        num2times[i] = num2idx[i] - seen[left_idx]
    seen.add(num2idx[i])

# print(num2times)

for i in range(1, N):
    dp[i] = (dp[i - 1] * num2times[Q[i]]) % MOD

# print(dp)
print(dp[-1])