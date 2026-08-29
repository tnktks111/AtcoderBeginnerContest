from itertools import accumulate

N, Q = map(int, input().split())

x_coords = []
y_coords = []

for _ in range(N):
    x, y = map(int, input().split())
    x_coords.append(x)
    y_coords.append(y)

gaiseki = []
x_dups = []
y_dups = []
for i in range(N):
    gaiseki.append(x_coords[i] * y_coords[(i + 1) % N] - x_coords[(i + 1) % N] * y_coords[i])
    x_dups.append((x_coords[i] + x_coords[(i + 1) % N]) * gaiseki[i])
    y_dups.append((y_coords[i] + y_coords[(i + 1) % N]) * gaiseki[i])

gaiseki_acc = [0] + list(accumulate(gaiseki))
x_dups_acc = [0] + list(accumulate(x_dups))
y_dups_acc = [0] + list(accumulate(y_dups))

def solve():
    u, v = map(int, input().split())
    if u < v:
        new_gaiseki = x_coords[v - 1] * y_coords[u - 1] - x_coords[u - 1] * y_coords[v - 1]
        A = (gaiseki_acc[v - 1] - gaiseki_acc[u - 1]) + new_gaiseki
        Cx = (x_dups_acc[v - 1] - x_dups_acc[u - 1]) + (x_coords[v - 1] + x_coords[u - 1]) * new_gaiseki
        Cx /= 3 * A
        Cy = (y_dups_acc[v - 1] - y_dups_acc[u - 1]) + (y_coords[v - 1] + y_coords[u - 1]) * new_gaiseki
        Cy /= 3 * A
        print(Cx, Cy)

    else:
        new_gaiseki = x_coords[v - 1] * y_coords[u - 1] - x_coords[u - 1] * y_coords[v - 1]
        A = (gaiseki_acc[v - 1] + gaiseki_acc[-1] - gaiseki_acc[u - 1]) + new_gaiseki
        Cx = (x_dups_acc[v - 1] + x_dups_acc[-1] - x_dups_acc[u - 1]) + (x_coords[v - 1] + x_coords[u - 1]) * new_gaiseki
        Cx /= 3 * A
        Cy = (y_dups_acc[v - 1] + y_dups_acc[-1] - y_dups_acc[u - 1]) + (y_coords[v - 1] + y_coords[u - 1]) * new_gaiseki
        Cy /= 3 * A
        print(Cx, Cy)


for _ in range(Q):
    solve()