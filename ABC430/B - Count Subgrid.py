N, M = map(int, input().split())
board = [input() for _ in range(N)]
possible = set()
for i in range(N - M + 1):
    for j in range(N - M + 1):
        tmp = []
        for k in range(M):
            tmp.append(board[i + k][j:j+M])
        possible.add("".join(tmp))
print(len(possible))
        