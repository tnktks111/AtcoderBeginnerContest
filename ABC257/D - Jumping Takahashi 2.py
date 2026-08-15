#二分探索
from collections import deque

def canMove(S, frm_idx, to_idx, x, y, P):
    dist = abs(x[frm_idx] - x[to_idx]) + abs(y[frm_idx] - y[to_idx])
    power = P[frm_idx]

    if power == 0:
        return dist == 0

    return power * S >= dist

def check(S, N, x, y, P):
    for start_node in range(N):
        visited = {start_node}
        queue = deque([start_node])
        while queue:
            current_node = queue.popleft()
            for next_node in range(N):
                if next_node not in visited and canMove(S, current_node, next_node, x, y, P):
                    visited.add(next_node)
                    queue.append(next_node)
        if len(visited) == N:
            return True
    return False

N = int(input())
x = [0] * N
y = [0] * N
P = [0] * N
for i in range(N):
    x[i], y[i], P[i] = map(int, input().split())

ng = -1
ok = 4 * 10**9 + 1

while ok - ng > 1:
    md = (ng + ok) // 2
    if check(md, N, x, y, P):
        ok = md
    else:
        ng = md

print(ok)


#Dijkstra法(o(n^3logn))
# from collections import defaultdict
# import heapq

# N = int(input())
# XYP = [list(map(int, input().split())) for _ in range(N)]
# edges = defaultdict(list)
# for i in range(N):
#     x1, y1 = XYP[i][:2]
#     jump = XYP[i][2]
#     for j in range(N):
#         if i == j:
#             continue
#         x2, y2 = XYP[j][:2]
#         dist = abs(x1 - x2) + abs(y1 - y2)
#         if dist % jump == 0:
#             edges[i].append((dist // jump, j))
#         else:
#             edges[i].append((dist // jump + 1, j))
# res = float("inf")
# for i in range(N):
#     cur_res = 0
#     minQ = [(0, i)]
#     visit = set()
#     while minQ:
#         w1, n1 = heapq.heappop(minQ)
#         if n1 in visit:
#             continue
#         visit.add(n1)
#         cur_res = max(w1, cur_res)
#         for w2, n2 in edges[n1]:
#             if n2 not in visit:
#                 heapq.heappush(minQ, (w2, n2))
#     res = min(cur_res, res)
# print(res)


# ワーシャルフロイド法(o(n^3))
# N = int(input())

# # 各点のデータ (x, y, p) をリストに格納
# data = []
# for _ in range(N):
#     x, y, p = map(int, input().split())
#     data.append((x, y, p))

# # 距離行列を初期化 (N x N)
# # dist[i][j] は点 i から点 j への初期コスト（到達に必要な最小ステップ数 S）
# dist = [[0] * N for _ in range(N)]
# # 初期コストを計算
# for i in range(N):
#     xi, yi, pi = data[i]
#     for j in range(N):
#         xj, yj, _ = data[j]
#         manhattan_dist = abs(xi - xj) + abs(yi - yj)
#         if pi == 0:
#             if manhattan_dist == 0:
#                 dist[i][j] = 0
#             else:
#                 dist[i][j] = float('inf') 
#         else:
#             dist[i][j] = (manhattan_dist + pi - 1) // pi

# # ワーシャル・フロイド法の考え方を応用した最小ボトルネック経路コストの計算
# # dist[i][j] を「iからjへ到達する経路上の最大コストの最小値」に更新していく
# for k in range(N): # 経由点 k
#     for i in range(N): # 始点 i
#         for j in range(N): # 終点 j
#             # i -> k -> j という経路のボトルネックコスト（最大コスト区間）
#             cost_via_k = max(dist[i][k], dist[k][j])
#             # 現在の i -> j のコストより、k経由のコストが小さければ更新
#             dist[i][j] = min(dist[i][j], cost_via_k)

# ans = float('inf')
# for i in range(N):
#     max_dist_from_i = 0
#     for j in range(N):
#         max_dist_from_i = max(max_dist_from_i, dist[i][j])
#     ans = min(ans, max_dist_from_i)
# print(ans)


# これはだめだったやつ(クラスカル法は無向グラフのみ)
# class UnionFind:
#     def __init__(self, n):
#         self.parent = list(range(n + 1))
#         self.rank = [1] * (n + 1)
#     def root(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.root(self.parent[x])  # 経路圧縮
#         return self.parent[x]

#     def connect(self, x, y) -> True:
#         root_x = self.root(x)
#         root_y = self.root(y)
#         if root_x == root_y:
#             return False
#         if self.rank[root_x] < self.rank[root_y]:
#            root_x, root_y = root_y, root_x
#         self.rank[root_x] += self.rank[root_y]
#         self.parent[root_y] = root_x
#         return True

# N = int(input())
# XYP = [list(map(int, input().split())) for _ in range(N)]
# edges = []
# unionfind = UnionFind(N)
# for i in range(N):
#     x1, y1 = XYP[i][:2]
#     jump = XYP[i][2]
#     for j in range(N):
#         if i == j:
#             continue
#         x2, y2 = XYP[j][:2]
#         dist = abs(x1 - x2) + abs(y1 - y2)
#         if dist % jump == 0:
#             edges.append((dist // jump, i, j))
#         else:
#             edges.append((dist // jump + 1, i, j))
# edges.sort()
# res = 0
# for power, i, j in edges:
#     if unionfind.connect(i, j):
#         res = power
# print(res)

#クラスカル法とダイクストラ法はちょっと似てる