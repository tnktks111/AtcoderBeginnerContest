N, Q = map(int, input().split())

P = list(map(lambda x: int(x) - 1, input().split()))

P_dash = [0] * N
for i, p in enumerate(P):
    P_dash[p] = i

P_is_genuine = True

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, y = query[1] - 1, query[2] - 1
        if P_is_genuine:
            P_dash[P[x]], P_dash[P[y]] = P_dash[P[y]], P_dash[P[x]]
            P[x], P[y] = P[y], P[x]
        else:
            P[P_dash[x]], P[P_dash[y]] = P[P_dash[y]], P[P_dash[x]]
            P_dash[x], P_dash[y] = P_dash[y], P_dash[x]
    else:
        if P_is_genuine:
            P_is_genuine = False
        else:
            P_is_genuine = True
    # print(P)
    # print(P_dash)

if P_is_genuine:
    for i in range(N):
        P[i] += 1
    print(*P)
else:
    for i in range(N):
        P_dash[i] += 1
    print(*P_dash)