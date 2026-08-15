from collections import deque
N, M = map(int, input().split())
P = set(list(map(int, input().split())))

q = deque()
res = []
for n in range(1, N+1):
    if n in P:
        q.append(n)
    else:
        res.append(n)
        while q:
            res.append(q.pop())
print(*res)