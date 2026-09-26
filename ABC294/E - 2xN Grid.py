from collections import deque
L, N_1, N_2 = map(int, input().split())

q1 = deque()
q2 = deque()

for _ in range(N_1):
    v, l = map(int, input().split())
    q1.append((v, l))

for _ in range(N_2):
    v, l = map(int, input().split())
    q2.append((v, l))

res = 0
while q1 and q2:
    v1, l1 = q1.popleft()
    v2, l2 = q2.popleft()
    if l1 < l2:
        if v1 == v2:
            res += l1
        q2.appendleft((v2, l2 - l1))
    elif l1 > l2:
        if v1 == v2:
            res += l2
        q1.appendleft((v1, l1 - l2))
    else:
        if v1 == v2:
            res += l1

print(res)
