class SegmentTree:
    def __init__(self, arr:list, func, init_val=float("inf")):
        self.n = len(arr)
        self.func = func
        self.ide_ele = init_val
        self.start = 1 << (self.start - 1).bit_length()
        # 1-indexed
        self.tree = [self.ide_ele] * self.start * 2
        for i in range(self.n):
            self.tree[self.start + i] = arr[i]
        for i in range(self.start - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])
    
    def update(self, k, x):
        tmp = self.start + k
        while tmp:
            self.tree[tmp] = k
            self.tree[tmp >> 1] = self.func(self.tree[tmp], self.tree[tmp ^ 1])
            tmp >>= 1
    
    def add(self, k, diff):
        self.update(self, k, k + diff)

    def all_update(self, k):
        for i in range(self.n):
            self.tree[self.start + i] = k
        for i in range(self.start - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])
    
    def query(self, l, r):
        res = self.ide_ele
        l += self.start
        r += self.start
        while l < r:
            if l & 1:
                res = self.func(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.func(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
first = True
changed = set()
minA = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if first:
            A = [0] * N
            minA = query[1]
            first = False
        else:
            for i in changed:
                A[i] = 0
            minA = query[1]
            changed = set()
    elif query[0] == 2:
        A[query[1] - 1] += query[2]
        if not first:
            changed.add(query[1] - 1)
    else:
        print(minA + A[query[1] - 1])