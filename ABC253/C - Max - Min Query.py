import heapq
from collections import defaultdict
Q = int(input())
MinQ = []
MaxQ = []
cnt = defaultdict(int)

for _ in range(Q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(MaxQ, -query[1])
        heapq.heappush(MinQ, query[1])
        cnt[query[1]] += 1
    elif query[0] == 2:
        cnt[query[1]] = max(0, cnt[query[1]] - query[2])
    else:
        while cnt[-MaxQ[0]] == 0:
            heapq.heappop(MaxQ)
        Max = -MaxQ[0]
        while cnt[MinQ[0]] == 0:
            heapq.heappop(MinQ)
        Min = MinQ[0]
        print(Max - Min)
# 大反省コード
# Q = int(input())
# querys = [tuple(map(int, input().split())) for _ in range(Q)]
# S = []
# num_to_idx = {}
# Max, Min = -float("inf"), float("inf")

# for i in range(Q):
#     if querys[i][0] == 1:
#         S.append([querys[i][1], 0])
# S.sort()
# for i in range(len(S)):
#     num_to_idx[S[i][0]] = i

# for i in range(Q):
#     if querys[i][0] == 1:
#         S[num_to_idx[querys[i][1]]][1] += 1
#         Max = max(Max, querys[i][1])
#         Min = min(Min, querys[i][1])
#     elif querys[i][0] == 2:
#         if querys[i][1] not in num_to_idx:
#             continue
#         S[num_to_idx[querys[i][1]]][1] = max(S[num_to_idx[querys[i][1]]][1] - querys[i][2], 0)
#         if not S[num_to_idx[querys[i][1]]][1]:
#             if Max == querys[i][1]:
#                 idx = num_to_idx[Max]
#                 while idx >= 0 and not S[idx][1]:
#                     idx -= 1
#                 if idx < 0:
#                     Max = -float("inf")
#                 else:
#                     Max = S[idx][0]
#             if Min == querys[i][1]:
#                 idx = num_to_idx[Min]
#                 while idx < len(S) and not S[idx][1]:
#                     idx += 1
#                 if idx >= len(S):
#                     Min = float("inf")
#                 else:
#                     Min = S[idx][0]
#     else:
#         print(Max - Min)

# def nibutan(n:int, l:list):
#     left, right = 0, len(l) - 1
#     while (right - left > 1):
#         mid = (left + right) // 2
#         if l[mid] <= n:
#             left = mid
#         else:
#             right = mid
#     return left
