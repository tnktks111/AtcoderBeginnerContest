N, M = map(int, input().split())
pair = [[False] * N for _ in range(N)]
for _ in range(M):
    query = list(map(int, input().split()))
    for i in range(1, query[0]):
        for j in range(i + 1, query[0] + 1):
            pair[query[i] - 1][query[j] - 1] = True
            pair[query[j] - 1][query[i] - 1] = True
for i in range(N - 1):
    for j in range(i + 1, N):
        if pair[i][j] == False:
            print("No")
            exit()
print("Yes")