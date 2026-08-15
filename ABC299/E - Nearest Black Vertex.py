from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N)]
must_white = set()
black_candidates = []
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
K = int(input())
for _ in range(K):
    p, d = map(int, input().split())
    p -= 1
    q = deque()
    seen = set()
    candidates = set()
    q.append(p)
    seen.add(p)
    for i in range(d + 1):
        for _ in range(len(q)):
            cur = q.popleft()
            if i == d:
                candidates.add(cur)
            else:
                must_white.add(cur)
                for nei in G[cur]:
                    if nei in seen:
                        continue
                    seen.add(nei)
                    q.append(nei)
    black_candidates.append(candidates)

res = ["1"] * N
for v in list(must_white):
    res[v] = "0"

for i in range(K):
    diff = black_candidates[i] - must_white
    if not diff:
        print("No")
        exit()
print("Yes")
print("".join(res))