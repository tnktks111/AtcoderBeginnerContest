from collections import defaultdict
N = int(input())
xy = list(map(int, input().split()) for _ in range(N))

res = 0
G = defaultdict(list)
counts = defaultdict(int)
for x, y in xy:
    G[x].append(y)
for Gx in G.values():
    for y1 in Gx:
        for y2 in Gx:
            if (y1 < y2):
                res += counts[(y1, y2)]
                counts[(y1, y2)] += 1
print(res)