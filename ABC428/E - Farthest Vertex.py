N = int(input())
G = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dp_lower = [[0, i] for i in range(N)]
parents = [0] * N

def dfs_lower(cur:int, parent:int):
    q = []
    q.append((cur, parent, 0))
    while q:
        c, p, phase = q.pop()
        if phase == 0:
            parents[c] = p
            q.append((c, p, 1))
            for nei in G[c]:
                if nei == p:
                    continue
                q.append((nei, c, 0))
        else:
            for nei in G[c]:
                if nei == p:
                    continue
                nei_dist = dp_lower[nei][0] + 1
                if nei_dist > dp_lower[c][0]:
                    dp_lower[c][0] = nei_dist
                    dp_lower[c][1] = dp_lower[nei][1]
                elif nei_dist == dp_lower[c][0]:
                    dp_lower[c][1] = max(dp_lower[c][1], dp_lower[nei][1])
                  
dfs_lower(0, -1)

children_info = [[] for _ in range(N)]
for i in range(N):
    max1 = [-1, -1]
    max2 = [-1, -1]
    for neighbor in G[i]:
        if neighbor == parents[i]:
            continue
        d = dp_lower[neighbor]
        if d[0] > max1[0] or (d[0] == max1[0] and d[1] > max1[1]):
            max2 = max1
            max1 = d
        elif d[0] > max2[0] or (d[0] == max2[0] and d[1] > max2[1]):
            max2 = d
    children_info[i] = [max1, max2]

dp_upper = [[0, i] for i in range(N)]
def dfs_upper(cur:int, parent:int):
    q = []
    q.append((cur, parent))
    while q:
        c, p = q.pop()
        if p != -1:
            if p != -1:
                bro_most_far_dist = -1
                bro_most_far_to = -1
                # print("at cur =", cur)
                if children_info[p] and children_info[p][0] != dp_lower[c]:
                    bro_most_far_dist, bro_most_far_to = children_info[p][0]
                elif len(children_info[p]) > 1:
                    bro_most_far_dist, bro_most_far_to = children_info[p][1]
                # if c == 2:
                    # print("debug", p, bro_most_far_dist, bro_most_far_to)
                if dp_upper[p][0] > bro_most_far_dist + 1:
                    dp_upper[c][0] = dp_upper[p][0] + 1
                    dp_upper[c][1] = dp_upper[p][1]
                elif dp_upper[p][0] < bro_most_far_dist + 1:
                    dp_upper[c][0] = bro_most_far_dist + 2
                    dp_upper[c][1] = bro_most_far_to
                else:
                    dp_upper[c][0] = bro_most_far_dist + 2
                    dp_upper[c][1] = max(bro_most_far_to, dp_upper[p][1])
            
        for child in G[c]:
            if child == p:
                continue
            q.append((child, c))
dfs_upper(0, -1)
# print(dp_upper)
# print(dp_lower)

res = []
for i in range(N):
    if dp_lower[i][0] > dp_upper[i][0]:
        res.append(dp_lower[i][1] + 1)
    elif dp_lower[i][0] < dp_upper[i][0]:
        res.append(dp_upper[i][1] + 1)
    else:
        res.append(max(dp_upper[i][1], dp_lower[i][1]) + 1)
print(*res, sep="\n")