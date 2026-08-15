from collections import defaultdict, deque
N = int(input())
adj = defaultdict(list)
indegree = dict()

unique_node = set()
for _ in range(N):
    dst, src = input().split()
    adj[src].append(dst)
    indegree[src] = indegree.get(src, 0)
    indegree[dst] = indegree.get(dst, 0) + 1
    unique_node.add(src)
    unique_node.add(dst)

q = deque()

for key, val in indegree.items():
    if val == 0:
        q.append(key)

changed = 0
while q:
    src = q.popleft()
    changed += 1
    for dst in adj[src]:
        indegree[dst] -= 1
        if indegree[dst] == 0:
            q.append(dst)
            
print("Yes" if changed == len(unique_node) else "No")
