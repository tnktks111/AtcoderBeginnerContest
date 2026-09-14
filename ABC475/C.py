from bisect import bisect_right

N, S, L = map(int, input().split())

A = list(map(int, input().split()))

S -= 1

if L == 0:
    print(1)
    exit()

if S == 0:
    dists = [0] * N
    for i in range(1, N):
        dists[i] = dists[i - 1] + A[i - 1]
    idx = bisect_right(dists, L) - 1
    print(idx + 1)    
elif S == N - 1:
    dists = [0] * N
    for i in range(1, N):
        dists[i] = dists[i - 1] + A[N - 1 - i]
    idx = bisect_right(dists, L) - 1
    print(idx + 1)
else:
    to_left = [0] * (N - S)
    to_right = [0] * (S + 1)
    for i in range(1, N - S):
        to_left[i] = to_left[i - 1] + A[S + i - 1]
    for i in range(1, S + 1):
        to_right[i] = to_right[i - 1] + A[S - i]

    res = -1
    res = max(bisect_right(to_left, L), res)
    res = max(bisect_right(to_right, L), res)

    # left first
    for i in range(1, N - S):
        tmp = i
        tmp_dist = to_left[i] * 2
        if tmp_dist > L:
            break
        idx = bisect_right(to_right, L - tmp_dist)
        tmp += idx
        res = max(res, tmp)

    for i in range(1, S + 1):
        tmp = i
        tmp_dist = to_right[i] * 2
        if tmp_dist > L:
            break
        idx = bisect_right(to_left, L - tmp_dist)
        tmp += idx
        res = max(res, tmp)
    print(res)