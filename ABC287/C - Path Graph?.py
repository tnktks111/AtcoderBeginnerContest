from collections import defaultdict

class UnionFind:
    def __init__(self, n:int):
        self.n = n 
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    def find(self, x:int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x:int, y:int):
        a, b = self.find(x), self.find(y)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        self.parent[b] = a
        return True

N, M = map(int, input().split())
uf = UnionFind(N)
in_dig = defaultdict(int)

for _ in range(M):
    u, v = map(int, input().split())
    in_dig[u] += 1
    in_dig[v] += 1
    uf.union(u - 1, v - 1)

if N - M != 1:
    print("No")
    exit()

group_cnt = 0
seen = set()
for i in range(N):
    root = uf.find(i)
    if root not in seen:
        group_cnt += 1
        seen.add(root)
if group_cnt != 1:
    print("No")
    exit()

cnt = {1:0, 2:0}
for item in in_dig.values():
    if item > 2:
        print("No")
        exit()
    cnt[item] += 1
print("Yes" if cnt[1] == 2 else "No")