from collections import deque
N, X = map(int, input().split())
res = X
S = input()
Q = deque()
for i in range(N):
    if S[i] == "U":
        if Q and Q[-1] != "U":
            Q.pop()
        else:
            Q.append("U")
    else:
        Q.append(S[i])
while Q:
    n = Q.popleft()
    if n == "U":
        res //= 2
    else:
        res *= 2
        if n == "R":
            res += 1
print(res)