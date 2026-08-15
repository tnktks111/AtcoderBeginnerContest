from collections import defaultdict
edge = defaultdict(lambda: False)

N, Q = map(int, input().split())
for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        edge[(a, b)] = True
    elif t == 2:
        edge[(a, b)] = False
    else:
        print("Yes" if edge[(a, b)] and edge[(b, a)] else "No")