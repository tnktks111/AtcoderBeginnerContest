# import sys
# sys.setrecursionlimit(10000)

# N = int(input())
# happiness = [[0] * (2 * N) for _ in range(2 * N)]

# # 入力を上三角部分に格納
# for i in range(2 * N - 1):
#     A = list(map(int, input().split()))
#     for j in range(i + 1, 2 * N):
#         happiness[i][j] = A[j - i - 1]
#         happiness[j][i] = A[j - i - 1]  # 対称にする

# used = [False] * (2 * N)
# res = 0

# def dfs(score):
#     global res
#     # すべての人を使ったら結果更新
#     if all(used):
#         res = max(res, score)
#         return
#     # 最初の未使用の人を選ぶ
#     for i in range(2 * N):
#         if not used[i]:
#             used[i] = True
#             break
#     # iとペアにできる他の未使用の人を探す
#     for j in range(i + 1, 2 * N):
#         if not used[j]:
#             used[j] = True
#             dfs(score ^ happiness[i][j])
#             used[j] = False
#     used[i] = False

# dfs(0)
# print(res)


N = int(input())
happiness = [[0] * (2 * N) for _ in range(2 * N - 1)]
for i in range(2 * N - 1):
    A = list(map(int, input().split()))
    for j in range(i + 1, 2 * N):
        happiness[i][j] = A[j - i - 1]

candidates = list(range(2 * N))
res = [0]
def perm_happiness(nums, haps):
    if len(nums) == 0:
        res[0] = max(res[0], haps)
        return

    first = nums[0]
    for idx in range(1, len(nums)):
        rest = nums[1:idx] + nums[idx+1:]
        perm_happiness(rest, haps ^ happiness[first][nums[idx]])

perm_happiness(candidates, 0)

print(res[0])

# 初回のコード
# elseのindex処理を間違えていた
# N = int(input())
# happiness = [[0] * (2 * N) for _ in range(2 * N - 1)]
# for i in range(2 * N - 1):
#     A = list(map(int, input().split()))
#     for j in range(i + 1, 2 * N):
#         happiness[i][j] = A[j - i - 1]

# candidates = list(range(2 * N))
# res = [0]
# def perm_happiness(nums, haps, remain):
#     if remain == 2:
#         res[0] = max(res[0], haps ^ happiness[nums[0]][nums[1]])
#     for idx in range(1, len(nums)):
#         if idx != len(nums) - 1:
#             rest = nums[1:idx] + nums[idx + 1:]
#         else:
#             rest = nums[1:-1]
#         perm_happiness(rest, haps ^ happiness[nums[0]][nums[idx]], remain - 2)

# perm_happiness(candidates, 0, 2 * N)

# print(res[0])