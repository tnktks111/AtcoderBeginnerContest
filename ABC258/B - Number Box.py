options = {0:"up", 1:"down", 2:"left", 3:"right", 4:"leftup", 5:"leftdown", 6:"rightup", 7:"rightdown"}

N = int(input())
A = []
MaxNum = 0
for _ in range(N):
    line = [int(n) for n in input()]
    A.append(line)
    MaxNum = max(MaxNum, max(line))

def line_num(r, c, N, option) -> int:
    res = []
    if option == "up":
        for i in range(N):
            res.append(A[r][(c - i) % N])
    if option == "down":
        for i in range(N):
            res.append(A[r][(c + i) % N])
    if option == "left":
        for i in range(N):
            res.append(A[(r - i) % N][c])
    if option == "right":
        for i in range(N):
            res.append(A[(r + i) % N][c])
    if option == "leftup":
        for i in range(N):
            res.append(A[(r - i) % N][(c - i) % N])
    if option == "leftdown":
        for i in range(N):
            res.append(A[(r - i) % N][(c + i) % N])
    if option == "rightup":
        for i in range(N):
            res.append(A[(r + i) % N][(c - i) % N])
    if option == "rightdown":
        for i in range(N):
            res.append(A[(r + i) % N][(c + i) % N])
    return (int("".join(map(str, res))))

starts = []
for i in range(N):
    for j in range(N):
        if A[i][j] == MaxNum:
            starts.append((i, j))
ans = 0
for i in range(len(starts)):
    r, c = starts[i]
    for i in range(8):
        ans = max(ans, line_num(r, c, N, options[i]))
print(ans)