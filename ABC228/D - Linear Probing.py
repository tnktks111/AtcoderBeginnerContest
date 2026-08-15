class UnionFind(): # Union-Find
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y): # 本問向けに改造
        self.parents[self.find(x)] = self.find(y)
            
mod = 1048576
uf = UnionFind(mod)
arr = [-1] * mod
Q = int(input())
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        h = x % mod
        next_h = uf.find(h)
        arr[next_h] = x
        uf.union(next_h, (next_h + 1) % mod)
    else:
        print(arr[x % mod])

# 最初に出したやつ
# mod = 1048576
# arr = [-1] * mod

# Q = int(input())
# for _ in range(Q):
#     t, x = map(int, input().split())
#     if t == 1:
#         idx = x % mod
#         while arr[idx] != -1:
#             idx = (idx + 1) % mod
#         arr[idx] = x
#     else:
#         print(arr[x % mod])