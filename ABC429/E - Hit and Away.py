from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
S = input()

safe = []
danger = []
danger_to_danger_idx = {}
danger_cnt = 0

q = deque()
for i, c in enumerate(S):
    if c == "S":
        q.append((i, -1, i, 0))
        safe.append(i)
    else:
        danger.append(i)

res = [[float("inf"), float("inf"), -1] for _ in range(N)]
for i in safe:
    res[i][0] = 0
    res[i][2] = i
nokori = len(danger)
seen = set()
while nokori > 0:
    for _ in range(len(q)):
        cur, parent, root, cost = q.popleft()
        for nei in G[cur]:
            if nei == parent:
                continue
            if res[nei][1] != float("inf"):
                continue
            elif res[nei][0] == float("inf"):
                res[nei][0] = cost + 1
                res[nei][2] = root
            elif res[nei][1] == float("inf"):
                if res[nei][2] == root:
                    continue
                res[nei][1] = cost + 1
                if S[nei] == "D":
                    nokori -= 1
            q.append((nei, cur, root, cost + 1))
# print(res)
for d in danger:
    print(res[d][0] + res[d][1])