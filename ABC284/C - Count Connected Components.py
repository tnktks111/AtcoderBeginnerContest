class myUnionFind:
    def __init__(self, n:int):
        self.n = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    def find(self, x:int):
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
        self.parent[b] = a
        self.size[b] += self.size[a]
        return True

N, M = map(int, input().split())
uf = myUnionFind(N)

for _ in range(M):
    u, v = map(lambda x: x-1, map(int, input().split()))
    uf.union(u, v)

seen = set()
res = 0
for i in range(N):
    root = uf.find(i)
    if root in seen:
        continue
    seen.add(root)
    res += 1
print(res)
