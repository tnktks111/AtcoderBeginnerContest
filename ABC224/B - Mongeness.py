H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
for i in range(H - 1):
    for j in range(W - 1):
        if grid[i][j] + grid[i+1][j+1] > grid[i][j+1] + grid[i+1][j]:
            print("No")
            exit()
print("Yes")