from collections import deque
Q = int(input())
cur = 0
q = deque()

paren_to_sign = { "(":1, ")":-1}
cur = 0
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        paren = query[1]
        if q:
            if q[-1][1] == False:
                q.append((q[-1][0] + paren_to_sign[paren], False))
            else:
                nxt = q[-1][0] + paren_to_sign[paren]
                q.append((nxt, (nxt >= 0)))
        else:
            nxt = paren_to_sign[paren]
            q.append((nxt, (nxt >= 0)))
    else:
        q.pop()
    print("Yes" if not q or (q[-1][1] == True and q[-1][0] == 0) else "No")