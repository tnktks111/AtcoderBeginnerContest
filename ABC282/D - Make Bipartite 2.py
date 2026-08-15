from collections import defaultdict

class myUnionFind:
    def __init__(self,n:int):
        self.n = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    def find(self, x:int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x:int, y:int):
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
G = defaultdict(list)
uf = myUnionFind(N)
connection_to_colormap = defaultdict(dict)
connection_to_colorcnt = defaultdict(lambda:[0, 0])
for _ in range(M):
    u, v = map(int, input().split())
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)
    uf.union(u - 1, v - 1)

graph_sizes = []
connection_first = set()
for i in range(N):
    root = uf.find(i)
    if root in connection_first:
        continue
    connection_first.add(root)
connection_first = list(connection_first)

for first in connection_first:
    graph_sizes.append(uf.size[first])
    connection_to_colormap[first][first] = 0
    connection_to_colorcnt[first][0] += 1
    stack = [first]
    seen = {first}
    while stack:
        newstack = []
        for node in stack:
            for adj in G[node]:
                if adj in seen:
                    if connection_to_colormap[first][adj] == connection_to_colormap[first][node]:
                        print(0)
                        exit()
                else:
                    if connection_to_colormap[first][node] == 1:
                        connection_to_colormap[first][adj] = 0
                        connection_to_colorcnt[first][0] += 1
                    else:
                        connection_to_colormap[first][adj] = 1
                        connection_to_colorcnt[first][1] += 1
                    seen.add(adj)
                    newstack.append(adj)
        stack = newstack

res = 0
left_graph_node = N
for i, first in enumerate(connection_first):
    res += connection_to_colorcnt[first][0] * connection_to_colorcnt[first][1]
    res += graph_sizes[i] * (left_graph_node - graph_sizes[i])
    left_graph_node -= graph_sizes[i]

print(res - M)