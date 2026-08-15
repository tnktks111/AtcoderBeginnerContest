from collections import defaultdict
import heapq

N, Q = map(int, input().split())

cnt = defaultdict(int)
cnt[0] = N
base = 0
le_base = N
A = [0] * N
tmp = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1] - 1
        
        if A[x] == base:
            le_base -= 1

        cnt[A[x]] -= 1
        A[x] += 1
        cnt[A[x]] += 1
        tmp ^= 1

    else:
        base += 1
        le_base += cnt[base]
        for _ in range(N - le_base):
            tmp ^= 1
    print(tmp)