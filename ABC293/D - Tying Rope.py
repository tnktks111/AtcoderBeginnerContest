class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.n = n
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        
        if a == b:
            return False
        
        if self.size[a] < self.size[b]:
            a, b = b, a
        
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

N, M = map(int, input().split())
uf = UnionFind(N)
cycle = 0
for _ in range(M):
    A, B, C, D = input().split()
    if not uf.union(int(A) - 1, int(C) - 1):
        cycle += 1

seen = set()
total = 0
for i in range(N):
    root = uf.find(i)
    if root not in seen:
        total += 1
        seen.add(root)
print(f"{cycle} {total - cycle}")