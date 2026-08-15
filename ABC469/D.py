N, M = map(int, input().split())

pairs = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
res = set()

a = pairs[0][0]
b = pairs[0][1]
remains = []
for pair in pairs:
    if a not in pair:
        remains.append(pair)
        
# すべてaを含む
if not remains:
    for i in range(N):
        if i > a:
            res.add((a, i))
        elif i < a:
            res.add((i, a))
else:
    c = remains[0][0]
    d = remains[0][1]
    have_c = True
    for remain in remains:
        if c not in remain:
            have_c = False
    if have_c:
        if a > c:
            res.add((c, a))
        else:
            res.add((a, c))
    have_d = True
    for remain in remains:
        if d not in remain:
            have_d = False
    if have_d:
        if a > d:
            res.add((d,a))
        else:
            res.add((a, d))

remains = []
for pair in pairs:
    if b not in pair:
        remains.append(pair)

if not remains:
    for i in range(N):
        if i > b:
            res.add((b, i))
        elif i < b:
            res.add((i, b))
else:
    c = remains[0][0]
    d = remains[0][1]
    have_c = True
    for remain in remains:
        if c not in remain:
            have_c = False
    if have_c:
        if b > c:
            res.add((c, b))
        else:
            res.add((b, c))
    have_d = True
    for remain in remains:
        if d not in remain:
            have_d = False
    if have_d:
        if b > d:
            res.add((d,b))
        else:
            res.add((b, d))

print(len(res))