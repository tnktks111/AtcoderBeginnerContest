from collections import deque
N = int(input())
S = input()
cur = 0
L, R = deque(), deque()

for i in range(N):
    if S[i] == "L":
        R.appendleft(cur)
    else:
        L.append(cur)
    cur += 1
L.append(cur)
L += R
print(*L)