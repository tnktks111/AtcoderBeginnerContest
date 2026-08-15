X = int(input())
N = int(input())
W = list(map(int, input().split()))
used = [False] * N
Q = int(input())
cur = X
for _ in range(Q):
    p = int(input()) - 1
    if used[p]:
        used[p] = False
        cur -= W[p]
    else:
        used[p] = True
        cur += W[p]
    print(cur)
    