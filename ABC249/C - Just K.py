N, K = map(int, input().split())
cnt = [[0] * 26 for _ in range(N)]
res = 0
for i in range(N):
    S = input()
    for j in range(len(S)):
        cnt[i][ord(S[j]) - ord("a")] += 1
for bin in range(1 << N):
    cur = [0] * 26
    cur_res = 0
    for i in range(N):
        if ((bin >> i) & 1):
            for j in range(26):
                cur[j] += cnt[i][j]
    for i in range(26):
        if cur[i] == K:
            cur_res += 1
    res = max(res, cur_res)
print(res)