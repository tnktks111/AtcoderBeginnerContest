HW = tuple(map(int, input().split()))
grid = [[0] * 3 for _ in range(3)]

res = [0]

def dfs(r, c) -> None:
    if r == 3:
        if grid[0][2] + grid[1][2] + grid[2][2] != HW[5]:
            return
        res[0] += 1
        return
    if r == 2 and c > 0:
        if grid[0][c - 1] + grid[1][c - 1] + grid[2][c - 1] != HW[3 + c - 1]:
            return

    if c == 2:
        grid[r][c] = HW[r] - sum(grid[r])
        dfs(r + 1, 0)
        grid[r][c] = 0
    else:
        for i in range(1, HW[r] - sum(grid[r]) - (2 - c) + 1):
            grid[r][c] = i
            dfs(r, c + 1)
            grid[r][c] = 0

dfs(0, 0)
print(res[0])



  