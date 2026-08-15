from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
A_cum = list(accumulate(A))
A_cumsum = []
A_cumsum.append(0)
for i in range(N):
    if i % 2 == 0:
        A_cumsum.append(A_cum[i // 2] * 2 - A[i // 2])
    else:
        A_cumsum.append(A_cum[i // 2] * 2)

dp = [0] * (N + 1)
# print(A_cumsum)
if N == 1:
    print(0)
    exit()
elif N == 2:
    print(A[0])
    exit()
for i in range(N + 1):
    # print(f"i = {i}")
    tmp = 0
    for j in range(i):
        # print(dp[j], A_cumsum[i - j - 1])
        tmp = max(tmp, dp[j] + A_cumsum[i - j - 1])
    dp[i] = tmp
# print(dp)
print(dp[-1])