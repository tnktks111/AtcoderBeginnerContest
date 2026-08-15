class Fenwick_tree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n
    def add(self, p, x):
        p += 1 #0-indexed -> 1-indexed(後の"長さ"処理のため)
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p #最下位ビット = "長さ"をindexに付加
    #閉区間[l, r]の部分和を返す関数
    def sum(self, l, r):
        r += 1
        return self._sum(r) - self._sum(l)
    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

Q = int(input())
querys = []
A = set()
for i in range(Q):
    tmp = list(map(int, input().split()))
    querys.append(tmp)
    A.add(tmp[1])
N = len(A)
A = list(A)
A.sort()
conv = dict()
for i in range(len(A)):
    conv[A[i]] = i
def bin_search_left(x_index, k):
    l, r = 0, x_index
    while 1 < r - l:
        mid  =(l + r) // 2
        if k <= ft.sum(mid, x_index):
            l = mid
        else:
            r = mid
    if k <= ft.sum(r, x_index):
        return r
    elif k <= ft.sum(l, x_index):
        return l
    else:
        return -1
def bin_search_right(x_index, k):
    l, r = x_index, N - 1
    while 1 < r - l:
        mid  = (l + r) // 2
        if k <= ft.sum(x_index, mid):
            r = mid
        else:
            l = mid
    if k <= ft.sum(x_index,l):
        return l
    elif k <= ft.sum(x_index, r):
        return r
    else:
        return -1
ft = Fenwick_tree(10 ** 6)
for i in range(Q):
    if querys[i][0] == 1:
        ft.add(conv[querys[i][1]], 1)
    elif querys[i][0] == 2:
        m = bin_search_left(conv[querys[i][1]], querys[i][2])
        if m == -1:
            print(-1)
        else:
            print(A[m])
    else:
        m = bin_search_right(conv[querys[i][1]], querys[i][2])
        if m == -1:
            print(-1)
        else:
            print(A[m])
# time out
# Q = int(input())
# stack = []
# for _ in range(Q):
#     query = list(map(int, input().split()))
#     if query[0] == 1:
#         if not stack:
#             stack.append(query[1])
#         else:
#             stack.append(query[1])
#             key = query[1]
#             j = len(stack) - 2
#             while j >= 0:
#                 if stack[j] > key:
#                     stack[j + 1] = stack[j]
#                     j -= 1
#                 else:
#                     break
#             stack[j + 1] = key
#     elif query[0] == 2:
#         x, k = query[1], query[2]
#         i = len(stack) - 1
#         while i >= 0 and stack[i] > x:
#             i -= 1
#         for _ in range(k - 1):
#             i -= 1
#         if i < 0:
#             print(-1)
#         else:
#             print(stack[i])
#     else:
#         x, k = query[1], query[2]
#         i = 0
#         while i < len(stack) and stack[i] < x:
#             i += 1
#         for _ in range(k - 1):
#             i += 1
#         if i >= len(stack):
#             print(-1)
#         else:
#             print(stack[i])