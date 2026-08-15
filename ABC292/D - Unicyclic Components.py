class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.size = [1] * N
        self.edge = [0] * N
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)

        if a == b:
            self.edge[a] += 1
            return False
        
        if self.size[a] < self.size[b]:
            a, b = b, a
        
        self.edge[a] += 1
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

    def meet_condition(self, n:int):
        return self.size[n] == self.edge[n]

N, M = map(int, input().split())
uf = UnionFind(N)

for _ in range(M):
    u, v = map(int, input().split())
    uf.union(u - 1, v - 1)

# print(uf.parent)

seen = set()
for i in range(N):
    root = uf.find(i)
    if root in seen:
        continue
    seen.add(root)
    if uf.meet_condition(root) == False:
        print("No")
        exit()
print("Yes")