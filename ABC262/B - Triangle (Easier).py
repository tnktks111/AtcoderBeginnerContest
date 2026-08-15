N, M = map(int, input().split())
connected = [[False] * N for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    connected[u][v] = True
    connected[v][u] = True

res = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if connected[i][j] and connected[j][k] and connected[k][i]:
                res += 1
print(res)