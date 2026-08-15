R, C = map(int, input().split())
grid = [tuple(map(int, input().split())) for _ in range(2)]
print(grid[R - 1][C - 1])