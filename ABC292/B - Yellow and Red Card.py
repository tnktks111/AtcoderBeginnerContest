N, Q = map(int, input().split())
penalty = [0] * N
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1 or query[0] == 2:
        penalty[query[1] - 1] += query[0]
    else:
        print("Yes" if penalty[query[1] - 1] >= 2 else "No")

