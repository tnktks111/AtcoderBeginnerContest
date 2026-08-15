S = input()
S_set = list(set(S))
S_cnt = {}
for i in range(len(S)):
    S_cnt[S[i]] = S_cnt.get(S[i], 0) + 1
for i in range(len(S_set)):
    if S_cnt[S_set[i]] == 1:
        print(S_set[i])
        exit()
print(-1)