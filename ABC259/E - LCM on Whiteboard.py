N = int(input())

keep_max = dict()

for i in range(N):
    m = int(input())
    for _ in range(m):
        p, e = map(int, input().split())
        if p not in keep_max:
            keep_max[p] = (i, e, True)
        else:
            if keep_max[p][1] < e:
                keep_max[p] = (i, e, True)
            elif keep_max[p][1] == e:
                keep_max[p] = (i, e, False)

i_change = set()
for k, (i, e, is_single) in keep_max.items():
    if is_single:
        i_change.add(i)
res = len(i_change)
if res != N:
    res += 1
print(res)