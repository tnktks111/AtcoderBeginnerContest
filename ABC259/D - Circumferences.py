import math

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    def root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def connect(self, x, y) -> True:
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
           root_x, root_y = root_y, root_x
        self.rank[root_x] += self.rank[root_y]
        self.parent[root_y] = root_x
        return True

def intersect(circle1:tuple, circle2:tuple) -> bool:
    x_1, y_1, r_1 = circle1
    x_2, y_2, r_2 = circle2
    center_dist_square = (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2
    if center_dist_square <= (r_1 + r_2) ** 2 and (r_1 - r_2) ** 2 <= center_dist_square:
        return True
    return False

N = int(input())
s_x, s_y, t_x, t_y = map(int, input().split())
circles = [tuple(map(int, input().split())) for _ in range(N)]

unionfind = UnionFind(N)

for i in range(N):
    for j in range(i + 1, N):
        if intersect(circles[i], circles[j]):
            unionfind.connect(i, j)

for i in range(N):
    x, y, r = circles[i]
    if (s_x - x) ** 2 + (s_y - y) ** 2 == r ** 2:
        s_idx = i
    if (t_x - x) ** 2 + (t_y - y) ** 2 == r ** 2:
        t_idx = i

print("Yes" if not unionfind.connect(s_idx, t_idx) else "No")