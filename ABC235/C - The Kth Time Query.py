from collections import defaultdict
N, Q = map(int, input().split())
A = list(map(int, input().split()))
numlist = defaultdict(list)
for i in range(N):
    numlist[A[i]].append(i + 1)
for _ in range(Q):
    x, k = map(int, input().split())
    if len(numlist[x]) < k:
        print(-1)
    else:
        print(numlist[x][k - 1])
