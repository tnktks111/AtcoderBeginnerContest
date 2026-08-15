N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.append(0)
A.append(float("inf"))
A.sort(reverse=True)

def bin_search(n:int):
    left, right = 0, len(A) - 1
    while left + 1 != right:
        mid = (left + right) // 2
        if A[mid] < n:
            right = mid
        else:
            left = mid
    while left < len(A) - 1 and A[left] == A[left + 1]:
        left += 1
    return left

for _ in range(Q):
    x = int(input())
    print(bin_search(x))


# ダメなヤツ
# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort(reverse=True)
# height_to_rank = {}
# for i in range(len(A)):
#     height_to_rank[A[i]] = i + 1
# cur = 0
# for h in range(A[0], A[-1], -1):
#     if h in A:
#         cur = height_to_rank[h]
#     else:
#         height_to_rank[h] = cur
# for _ in range(Q):
#     x = int(input())
#     if x > A[0]:
#         print(0)
#     elif x < A[-1]:
#         print(N)
#     else:
#         print(height_to_rank[x])