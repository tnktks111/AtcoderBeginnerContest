from collections import deque

a, N = map(int, input().split())
Q = deque()
seen = set()
Q.append(N)

def rotate(n: int):
    n = str(n)
    if len(n) == 1:
        return (int(n))
    n = n[1:] + n[0]
    return(int(n))

res = 0
cnt = -1
while Q:
    cnt += 1
    for _ in range(len(Q)):
        cur = Q.popleft()
        if cur in seen:
            continue
        seen.add(cur)
        if cur == 1:
            print(cnt)
            exit()
        if len(str(cur)) == len(str(rotate(cur))):
            Q.append(rotate(cur))
        if cur > 0 and cur % a == 0:
            Q.append(cur // a)
print(-1)
