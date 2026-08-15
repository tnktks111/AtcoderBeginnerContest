N = int(input())
S0 = list(list(input()) for _ in range(N))
T = list(list(input()) for _ in range(N))

def turn90(grid, n):
    new_grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "#":
                new_grid[j][n - 1 - i] = "#"
            else:
                new_grid[j][n - 1 - i] = "."
    return new_grid

def move_to_corner(grid, n):
    new_grid = [["."] * n for _ in range(n)]
    flag = 0
    minrow = 0
    mincol = 0
    for i in range(n):
        for j in range(n):
            if flag == 0 and grid[i][j] == "#":
                minrow = i
                flag = 1
    flag = 0
    for j in range(n):
        for i in range(n):
            if flag == 0 and grid[i][j] == "#":
                mincol = j
                flag = 1
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "#":
                new_grid[i - minrow][j - mincol] = "#"
    return new_grid

def is_equal(grid1, grid2, n):
    for i in range(n):
        for j in range(n):
            if (grid1[i][j] != grid2[i][j]):
                return False
    return True

T = move_to_corner(T, N)
S1 = turn90(S0, N)
S2 = turn90(S1, N)
S3 = turn90(S2, N)
S0 = move_to_corner(S0, N)
S1 = move_to_corner(S1, N)
S2 = move_to_corner(S2, N)
S3 = move_to_corner(S3, N)
if is_equal(T, S0, N) or is_equal(T, S1, N) or is_equal(T, S2, N) or is_equal(T, S3, N):
    print("Yes")
else:
    print("No")