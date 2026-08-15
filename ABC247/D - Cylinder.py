from collections import deque
Q = int(input())
dq = deque()
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        dq.append((query[1], query[2]))
    else:
        res = 0
        remain = query[1]
        while remain:
            x, c = dq.popleft()
            if c > remain:
                dq.appendleft((x, c - remain))
                res += x * remain
                remain = 0
            else:
                res += x * c
                remain -= c
        print(res)