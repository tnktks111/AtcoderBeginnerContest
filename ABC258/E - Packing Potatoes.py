from itertools import accumulate
from bisect import bisect_left

N, Q, X = map(int, input().split())
W = list(map(int, input().split()))


acc_w = [0] * (2 * N + 1)
for i in range(1, 2 * N + 1):
    acc_w[i] = acc_w[i - 1] + W[(i - 1) % N]

dp = [[0] * N for _ in range(41)]
for i in range(N):
    left = X % acc_w[N]
    dp[0][i] = bisect_left(acc_w, left + acc_w[i]) % N

for i in range(1, 41):
    for j in range(N):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]

def solve(k:int):
    answer = 0
    i = 0
    k -= 1
    while k:
        if k & 1:
            answer = dp[i][answer]
        k >>= 1
        i += 1
    # print("answer", answer)
    # print(dp[0])
    p, q = divmod(X, acc_w[N])
    nxt = dp[0][answer]
    if nxt > answer:
        return N * p + nxt - answer
    elif nxt < answer:
        return N * p + nxt + N - answer
    else:
        if q:
            return N * (p + 1)
        else:
            return N * p

for _ in range(Q):
    K = int(input())
    print(solve(K))