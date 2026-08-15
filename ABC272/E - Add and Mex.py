import math
N, M = map(int, input().split())
A = list(map(int, input().split()))
possible_nums = [set() for _ in range(M)]
for i in range(N):
    start = max(1, math.ceil(-A[i] / (i + 1)))
    end = min(M, math.floor((N - A[i]) / (i + 1)))
    # print(start, end)
    if start <= end:
        for j in range(start, end + 1):
            possible_nums[j - 1].add(A[i] + (i + 1) * j)
#     print(possible_nums)
# print(possible_nums)
for i in range(M):
    for j in range(N + 1):
        if j not in possible_nums[i]:
            print(j)
            break
