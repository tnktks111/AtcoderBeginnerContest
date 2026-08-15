class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    def root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])  # 経路圧縮
        return self.parent[x]
    def connect(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

N, M = map(int, input().split())
G = [[] for _ in range(N)]
deg = [0] * N

uf = UnionFind(N)

for _ in range(M):
    a, b = map(int, input().split())
    deg[a - 1] += 1
    deg[b - 1] += 1
    if deg[a - 1] > 2 or deg[b - 1] > 2 or uf.root(a - 1) == uf.root(b - 1):
        print("No")
        exit()
    uf.connect(a - 1, b - 1)
print("Yes")