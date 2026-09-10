import heapq

N = int(input())
X = list(map(lambda x: int(x) - 1, input().split()))
C = list(map(int, input().split()))

indegree = [0] * N
edges = list(zip(range(N), X, C))
edges.sort(key=lambda x: x[2])
nxt_edge = 0

for i in range(N):
    indegree[X[i]] += 1

stack = []
seen = set()

for i in range(N):
    if indegree[i] == 0:
        stack.append(i)
        seen.add(i)

res = 0
# print(stack)
while True:
    if not stack:
        while nxt_edge < N and edges[nxt_edge][0] in seen:
            nxt_edge += 1
        if nxt_edge < N:
            res += edges[nxt_edge][2]
            indegree[edges[nxt_edge][1]] -= 1
            assert indegree[edges[nxt_edge][1]] == 0
            seen.add(edges[nxt_edge][1])
            stack.append(edges[nxt_edge][1])
    if not stack:
        break
    cur = stack.pop()
    nei = X[cur]
    indegree[nei] -= 1
    if indegree[nei] == 0:
        seen.add(nei)
        stack.append(nei)

print(res)