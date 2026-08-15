class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
        self.eat = [-1] * (n + 1)
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

def bin_search_and_insert(n:int, t:int, field:list) -> int:
        if not field or n > field[-1]:
            field.append(n)
            return
        if n <= field[0]:
            uf.connect(field[0], n)
            field[0] = n
            if uf.rank[uf.root(n)] == K:
                uf.eat[uf.root(n)] = t
                field.pop(0)
            return
        left, right = 0, len(field) - 1
        while right - left > 1:
            mid = (right + left) // 2
            if field[mid] >= n:
                right = mid
            else:
                left = mid
        uf.connect(field[right], n)
        field[right] = n
        if uf.rank[uf.root(n)] == K:
            uf.eat[uf.root(n)] = t
            field.pop(right)
        return

N, K = map(int, input().split())
P = list(map(int, input().split()))

if K == 1:
    num_to_idx = {}
    for i in range(N):
        num_to_idx[P[i]] = i + 1
    for i in range(1, N + 1):
        print(num_to_idx[i])
else:
    field = []
    uf = UnionFind(N)
    for i in range(N):
        bin_search_and_insert(P[i], i + 1, field)
    for i in range(1, N + 1):
        print(uf.eat[uf.root(i)])
