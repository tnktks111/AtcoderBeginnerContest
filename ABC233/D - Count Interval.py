from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * (N + 1)
for i in range(1, N + 1):
    S[i] = S[i - 1] + A[i - 1]
res = 0
cnt = defaultdict(int)
for i in range(N + 1):
    res += cnt[S[i] - K]
    cnt[S[i]] += 1
print(res)

# 総当たり(TLE)
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# memo = [0] * N
# ans = 0
# for i in range(N):
#     if i == 0:
#         memo[i] = A[i]
#     else:
#         memo[i] = memo[i - 1] + A[i]
#     if memo[i] == K:
#         ans += 1
# for i in range(1, N):
#     for j in range(i, N):
#         memo[j] = memo[j] - A[i - 1]
#         if memo[j] == K:
#             ans += 1
# print(ans)