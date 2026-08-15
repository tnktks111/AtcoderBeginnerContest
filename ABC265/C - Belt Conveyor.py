H, W = map(int, input().split())
G = [input() for _ in range(H)]

directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
cur = (0, 0)
seen = set()
while True:
    # print(cur)
    x, y = cur
    if cur in seen:
        print(-1)
        exit()
    seen.add(cur)
    dx, dy = directions[G[x][y]]
    if 0 <= x + dx < H and 0 <= y + dy < W:
        cur = (x + dx, y + dy)
    else:
        break
x, y = cur
x += 1
y += 1
print(x, y)
