N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

grid = [["."] * (S - R + 1) for _ in range(Q - P + 1)]

def is_black(x, y, n, a, b):
    if x - y == a - b and max(a - b, 0) < x <= min(n, n + a - b):
        return True
    elif x + y == a + b and max(a + b - n, 1) <= x <= min(a + b - 1, n):
        return True
    return False

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if is_black(P + r, R + c, N, A, B):
            grid[r][c] = "#"

for r in range(len(grid)):
    print("".join(grid[r]))
