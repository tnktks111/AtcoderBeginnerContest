S = [input() for _ in range(9)]
pones = []
for i in range(9):
    for j in range(9):
        if S[i][j] == "#":
            pones.append((i, j))

n = len(pones)
pones_set = set(pones)
res = set()
for i in range(n - 1):
    for j in range(i + 1, n):
        p, q = pones[i], pones[j]
        normal = [(p[1] - q[1], -p[0] + q[0]), (-p[1] + q[1], p[0] - q[0])]
        for dx, dy in normal:
            r = (p[0] + dx, p[1] + dy)
            s = (q[0] + dx, q[1] + dy)
            if r in pones_set and s in pones_set:
                res.add(tuple(sorted((p, q, r, s))))
print(len(res))