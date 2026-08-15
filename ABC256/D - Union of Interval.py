from collections import defaultdict
N = int(input())
sections = [list(map(int, input().split())) for _ in range(N)]
mp = defaultdict(int)
for start, end in sections:
    mp[start] += 1
    mp[end] -= 1

res = []
section = []
active = 0
for i in sorted(mp):
    if not section:
        section.append(i)

    active += mp[i]
    if active == 0:
        section.append(i)
        res.append(section)
        section = []

for sec in res:
    print(*sec)
