from sortedcontainers import SortedList

L, Q = map(int, input().split())
woods = SortedList([0, L])

for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        woods.add(x)
    else:
        r = woods.bisect_left(x)
        print(woods[r] - woods[r - 1])
