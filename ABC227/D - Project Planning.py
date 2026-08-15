# 逆転の発想(可能なプロジェクト数から考える)と二分探索
N, K = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = sum(A) // K + 1
ans = 0
while left <= right:
    mid = (right - left) // 2 + left
    res = sum(min(mid, a) for a in A)
    if mid * K <= res:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)



# 最初に書いたコード(TimeOut)
# import heapq
# N, K = map(int, input().split())
# A = [-x for x in map(int, input().split())]

# heapq.heapify(A)

# projects = 0
# while len(A) >= K:
#     departments = [heapq.heappop(A) for _ in range(K)]
#     projects += 1
#     for department in departments:
#         if department != -1:
#             heapq.heappush(A, department + 1)
# print(projects)