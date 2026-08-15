class UnionFind():
    def __init__(self, n:int):
        self.n = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x:int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x:int, y:int) -> bool:
        a = self.find(x)
        b = self.find(y)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = self.parent[a]
        self.size[a] += self.size[b]
        return True

N, M = map(int, input().split())
edges = 0
uf = UnionFind(N)
for _ in range(M):
    a, b = map(int, input().split())
    if uf.find(a - 1) != uf.find(b - 1):
        uf.union(a - 1, b - 1)
        edges += 1
print(M - edges)
