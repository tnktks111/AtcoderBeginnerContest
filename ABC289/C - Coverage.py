N, M = map(int, input().split())
S = []
ans = {i for i in range(1, N+1)}
res = 0
for _ in range(M):
    _ = int(input())
    S.append(set(list(map(int, input().split()))))
for i in range(2 ** M):
    cur = set()
    for j in range(M):
        if i & (1 << j):
            cur |= S[j]
    if cur == ans:
        res += 1
print(res)
