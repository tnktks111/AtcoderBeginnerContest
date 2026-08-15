N, M = map(int, input().split())
S = [int(input()) for _ in range(N)]
T_tail = [False] * 1000
res = 0
for _ in range(M):
    T_tail[int(input())] = True
for s in S:
    if T_tail[s % 1000]:
        res += 1
print(res)