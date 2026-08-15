from collections import deque

M = int(input())
ans = (0,1,2,3,4,5,6,7,8)
cnt = 0
seen = set()
adj = [[] for _ in range(9)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)
P = list(map(int, input().split()))
first = [8] * 9
for i in range(8):
    first[P[i] - 1] = i

first = tuple(first)
Q = deque()
Q.append(first)
seen.add(first)

while(Q):
    for _ in range(len(Q)):
        cur = Q.popleft()
        if cur == ans:
            print(cnt)
            exit()
        blank = cur.index(8)
        for nei in adj[blank]:
            nxt = list(cur)
            nxt[blank], nxt[nei] = nxt[nei], nxt[blank]
            nxt = tuple(nxt)
            if nxt not in seen:
                Q.append(nxt)
                seen.add(nxt)
    cnt += 1
print(-1)