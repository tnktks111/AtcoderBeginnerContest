grid = [input() for _ in range(2)]

a = None
d = None
for r in range(2):
    for c in range(2):
        if grid[r][c] == "A":
            a = (r, c)
        if grid[r][c] == "D":
            d = (r, c)

if a[0] + d[0] == 1 and a[1] + d[1] == 1:
    print("No")
else:
    print("Yes")