class myUnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
    def find(self,x:int):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x:int, y:int):
        a = self.find(x)
        b = self.find(y)
        if a == b:
            return False
        if self.sizes[a] < self.sizes[b]:
            a, b = b, a
        self.parents[b] = a
        self.sizes[a] += b
        self.n -= 1

    def get_self_size(self):
        return self.n

N = int(input())

uf = myUnionFind(N)
seen = set()
point_to_idx = {}
directions = [(1, 1), (1, 0), (0, -1), (-1, -1), (-1, 0), (0, 1)]
for i in range(N):
    x, y = map(int, input().split())
    for dx, dy in directions:
        if (x + dx, y + dy) in seen:
            uf.union(i, point_to_idx[(x + dx, y + dy)])
    point_to_idx[(x, y)] = i
    seen.add((x, y))
print(uf.get_self_size())