
N = int(input())
A = list(map(int, input().split()))
res = N * (N - 1) * (N - 2) // 6
cnt = {}
for i in range(N):
    cnt[A[i]] = cnt.get(A[i], 0) + 1
for k, v in cnt.items():
    if v >= 3:
        res -= v * (v - 1) * (v - 2) // 6
    if v >= 2:
        res -= v * (v - 1) * (N - v) // 2
print(res)

# TLE
# N = int(input())
# A = list(map(int, input().split()))
# cnt = {}
# for i in range(N):
#     cnt[A[i]] = cnt.get(A[i], 0) + 1
# cnt2 = [(k, v) for k, v in cnt.items()]

# res = 0
# for i in range(len(cnt2) - 2):
#     for j in range(i + 1, len(cnt2) - 1):
#         for k in range(j + 1, len(cnt2)):
#             res += cnt2[i][1] * cnt2[j][1] * cnt2[k][1]
# print(res)