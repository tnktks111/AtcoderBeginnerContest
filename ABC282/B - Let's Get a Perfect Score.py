N, M = map(int, input().split())
ability = [input() for _ in range(N)]
def can_solve(a:int, b:int):
    for i in range(M):
        if ability[a][i] == "x" and ability[b][i] == "x":
            return False
    return True

res = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if can_solve(i, j):
            res += 1
print(res)
