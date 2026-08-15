N, M = map(int, input().split())

koma = [tuple(map(int, input().split())) for _ in range(M)]
koma.reverse()
r_used = set()
c_used = set()

res = 0

for r, c in koma:
    if r not in r_used and c not in c_used:
        res += 1
    r_used.add(r)
    c_used.add(c)

print(res)