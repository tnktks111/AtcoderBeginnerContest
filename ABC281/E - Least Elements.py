class Fenwick_Tree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n
    
    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
    
    def sum(self, l, r):
        """
        [l, r)の区間和を返す
        """
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)
    
    def _sum(self, r):
        """
        [0, r)の区間和を返す
        """
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s
    
    def lower_bound(self, w):
        """
        _sum(x) < w となる最大の x を返す
        
        注意: すべての要素が非負の場合にのみ正しく動作する。
        """
        if w <= 0:
            return 0 # _sum(0) = 0 なので w <= 0 の条件を満たせない
        
        x = 0
        len = 1
        while len < self._n:
            len <<= 1
        while len > 0:
            if x + len <= self._n and self.data[x + len - 1] < w:
                w -= self.data[x + len - 1]
                x += len
            len >>= 1
        return x
    
    def upper_bound(self, w):
        """
        _sum(x) <= w となる最大の x を返す
        つまり _sum(x) > w となる最小の x を返す。
        
        注意: すべての要素が非負の場合にのみ正しく動作する。
        """
        if w < 0:
            return 0
        x = 0
        len = 1
        while len < self._n:
            len <<= 1
        while len > 0:
            if x + len <= self._n and self.data[x + len - 1] <= w:
                w -= self.data[x + len - 1]
                x += len
            len >>= 1
        return x

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
vals = sorted(list(set(A)))
V = len(vals)
num_to_idx = {vals[i]: i for i in range(V)}

total_sum = Fenwick_Tree(V)
cnt_tree = Fenwick_Tree(V)
res = []
for i in range(N):
    idx = num_to_idx[A[i]]
    total_sum.add(idx, A[i])
    cnt_tree.add(idx, 1)
    if i >= M:
        idx_prev = num_to_idx[A[i - M]]
        total_sum.add(idx_prev, -A[i - M])
        cnt_tree.add(idx_prev, -1)
    if i >= M - 1:
        j = cnt_tree.lower_bound(K)
        if j >= V:
            exit()
        res.append(total_sum.sum(0, j) + (K - cnt_tree.sum(0, j)) * vals[j])
print(*res)