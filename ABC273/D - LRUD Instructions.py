from collections import defaultdict
from sortedcontainers import SortedList
H, W, r, c = map(int, input().split())
row_wall = defaultdict(lambda: SortedList([0, W + 1]))
col_wall = defaultdict(lambda: SortedList([0, H + 1]))
N = int(input())

for _ in range(N):
    row, col = map(int, input().split())
    row_wall[row].add(col)
    col_wall[col].add(row)

def nibutan_left(L:SortedList, target:int):
    ok = -1
    ng = len(L)
    while (ng - ok > 1):
        mid = (ok + ng) // 2
        if L[mid] <= target:
            ok = mid
        else:
            ng = mid
    return (L[ok])

def nibutan_right(L:SortedList, target:int):
    ok = len(L)
    ng = -1
    while (ok - ng > 1):
        mid = (ok + ng) // 2
        if L[mid] >= target:
            ok = mid
        else:
            ng = mid
    return (L[ok])

Q = int(input())
cur = [r, c]
for _ in range(Q):
    d, l = input().split()
    l = int(l)
    if d == "U":
        near_kabe = nibutan_left(col_wall[cur[1]], cur[0])
        if cur[0] - l > near_kabe:
            cur[0] -= l
        else:
            cur[0] = near_kabe + 1
    elif d == "D":
        near_kabe = nibutan_right(col_wall[cur[1]], cur[0])
        if cur[0] + l < near_kabe:
            cur[0] += l
        else:
            cur[0] = near_kabe - 1
    elif d == "L":
        near_kabe = nibutan_left(row_wall[cur[0]], cur[1])
        if cur[1] - l > near_kabe:
            cur[1] -= l
        else:
            cur[1] = near_kabe + 1
    else:
        near_kabe = nibutan_right(row_wall[cur[0]], cur[1])
        if cur[1] + l < near_kabe:
            cur[1] += l
        else:
            cur[1] = near_kabe - 1
    print (*cur)
    