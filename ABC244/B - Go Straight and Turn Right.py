N, T = int(input()), input()
ESWN = [0] * 4
points = [0, 0]
cur = 0
for i in range(N):
    if T[i] == "S":
        ESWN[cur] += 1
    else:
        cur = (cur + 1) % 4
points[0] = ESWN[0] - ESWN[2]
points[1] = - ESWN[1] + ESWN[3]
print(*points)