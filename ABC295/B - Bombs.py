R, C = map(int, input().split())
board = []

for i in range(R):
    board.append(list(input()))

def explode(r, c, n, R, C):
    board[r][c] = "."
    for m in range(1,n+1):
        for i in range(-m, m+1):
            j = m - abs(i)
            if 0 <= r + i < R and 0 <= c + j < C and board[r+i][c+j]=="#":
                board[r+i][c+j] = "."
            j *= -1
            if 0 <= r + i < R and 0 <= c + j < C and board[r+i][c+j]=="#":
                board[r+i][c+j] = "."

for r in range(R):
    for c in range(C):
        if board[r][c].isdigit():
            n = int(board[r][c])
            explode(r, c, n, R, C)

for r in range(R):
    print("".join(board[r]))

