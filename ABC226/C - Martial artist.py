# heapqを使った解答
import heapq
N = int(input())
visited = [False] * N
martials = {}
for i in range(N):
    martials[i+1] = tuple(map(int, input().split()))

res = 0
Maxheap = []
heapq.heappush(Maxheap, -N)

while(Maxheap):
    cur = -heapq.heappop(Maxheap)
    if visited[cur - 1]:
        continue
    visited[cur - 1] = True
    res += martials[cur][0]
    if martials[cur][1] > 0:
        for i in range(martials[cur][1]):
            heapq.heappush(Maxheap, -martials[cur][2 + i])
print(res)


# #メモ化+dfs

# import sys
# sys.setrecursionlimit(1 << 25)

# N = int(input())
# T = [0] * (N + 1)
# deps = [[] for _ in range(N + 1)]

# for i in range(1, N + 1):
#     tmp = list(map(int, input().split()))
#     T[i] = tmp[0]
#     k = tmp[1]
#     deps[i] = tmp[2:]

# memo = [-1] * (N + 1)

# def dfs(i):
#     if memo[i] != -1:
#         return 0  # すでにこの技の修練時間はカウント済
#     total = 0
#     for pre in deps[i]:
#         total += dfs(pre)
#     memo[i] = T[i]
#     return total + memo[i]

# print(dfs(N))
