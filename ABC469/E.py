N, K = map(int, input().split())
S = input()
INF = float("inf")

idx2winnum = dict()
winnum2idx = []
win_num = 0

for i in range(N):
    if S[i] == "o":
        idx2winnum[i] = win_num
        winnum2idx.append(i)
        win_num += 1

def possible(rate:float, s:str, idx2winnum:dict, winnum2idx:list):
    # min_prefix[i] ... k∈[0, i)に対するaccumulationの最小値
    min_prefix = [0.0] * (N + 1)
    accumulation = [0] * (N + 1)
    cur = 0
    for i in range(N):
        if s[i] == "o":
            cur += (1 - rate)
        else:
            cur += (-rate)
        accumulation[i + 1] = cur
        min_prefix[i + 1] = min(min_prefix[i], cur)
    
    for r in range(N):
        if S[r] == "o":
            right_win_num = idx2winnum[r]
            if right_win_num < K - 1:
                continue
            left_win_num_sup = right_win_num - K + 1
            if min_prefix[winnum2idx[left_win_num_sup]] <= accumulation[r + 1]:
                return True

    return False

l = 0.0
r = 1.0
while r - l >= 10.0 ** (-7):
    m = (l + r) / 2
    if possible(m, S, idx2winnum, winnum2idx):
        l = m
    else:
        r = m
print(l)