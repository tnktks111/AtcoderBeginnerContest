from collections import deque
N = int(input())
A = list(map(int, input().split()))
Q = deque()
for i in range(N):
    if not Q:
        Q.append((A[i], 1))
    else:
        if Q[-1][0] == A[i]:
            Q.append((A[i], Q[-1][1] + 1))
            if Q[-1][0] == Q[-1][1]:
                for _ in range(Q[-1][0]):
                    Q.pop()
        else:
            Q.append((A[i], 1))
    print(len(Q))