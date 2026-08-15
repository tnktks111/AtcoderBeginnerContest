N, K = map(int, input().split())
P = [sum(map(int, input().split())) for _ in range(N)]
P_max = [p + 300 for p in P]
P.sort(reverse=True)

score_to_rank = {}
for i in range(len(P)):
    if i > 0 and P[i - 1] == P[i]:
        score_to_rank[P[i]] = score_to_rank[P[i - 1]]
    else:
        score_to_rank[P[i]] = i + 1

for s in range(P[-1], P[0]):
    if s in P:
        tmp = score_to_rank[s]
    else:
        score_to_rank[s] = tmp

for i in range(N):
    if P_max[i] > P[0]:
        rank = 1
    else:
        rank = score_to_rank[P_max[i]]
    if rank <= K:
        print("Yes")
    else:
        print("No")
