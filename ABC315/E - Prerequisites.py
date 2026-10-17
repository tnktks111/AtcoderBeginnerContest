N = int(input())

adj = [[] for _ in range(N)]
rev_adj = [[] for _ in range(N)]
indegree = [0] * N

for i in range(N):
    _, *prerequisites = map(lambda x: int(x) - 1, input().split())
    for pre in prerequisites:
        adj[pre].append(i)
        rev_adj[i].append(pre)
        indegree[i] += 1

# print(*adj, sep="\n")


stack = [0]
seen = {0}
starts = []

while stack:
    cur = stack.pop()
    if not rev_adj[cur]:
        starts.append(cur)
    for nei in rev_adj[cur]:
        if nei in seen:
            continue
        seen.add(nei)
        stack.append(nei)

res = []
must_read_set = seen.copy()
seen = {starts[0]}

# print(starts)
# print(*indegree)
while starts:
    cur = starts.pop()
    res.append(cur + 1)
    for nei in adj[cur]:
        if nei not in must_read_set:
            continue
        if nei in seen:
            continue
        indegree[nei] -= 1
        if indegree[nei] == 0:
            seen.add(nei)
            starts.append(nei)
print(*res[:-1])
