from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N)]
indegree = [0] * N
for _ in range(M):
    k = int(input())
    A = list(map(int, input().split()))
    for src, dst in zip(A, A[1:]):
        src -= 1
        dst -= 1
        indegree[dst] += 1
        adj[src].append(dst)
    
q = deque()
for i in range(N):
    if indegree[i] == 0:
        q.append(i)

finish = 0
while q:
    node = q.popleft()
    finish += 1
    for nei in adj[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            q.append(nei)
      
if finish == N:
    print('Yes')
else:
    print('No')