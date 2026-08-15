import itertools

N, M = map(int, input().split())
G_t = [[False] * N for _ in range(N)]
G_a = [[False] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G_t[a - 1][b - 1] = True
    G_t[b - 1][a - 1] = True
for _ in range(M):
    a, b = map(int, input().split())
    G_a[a - 1][b - 1] = True
    G_a[b - 1][a - 1] = True
ans = False
for p in itertools.permutations(range(N)):
    ok = True
    for i in range(N):
        for j in range(N):
            if G_t[i][j] != G_a[p[i]][p[j]]:
                ok = False
    if ok:
        ans = True
print("Yes" if ans else "No")