from collections import deque
S = input()
N = len(S)
seen_alpha_cnt = [0] * (N + 1)

q = deque()
q.append(-1)

for i in range(N):
    # print(q)
    # print(seen_alpha_cnt)
    if S[i].isalpha():
        if seen_alpha_cnt[i] & (1 << (ord(S[i]) - ord("a"))):
            print("No")
            exit()
        else:
            seen_alpha_cnt[i + 1] = seen_alpha_cnt[i] | (1 << (ord(S[i]) - ord("a")))
    elif S[i] == "(":
        q.append(i)
        seen_alpha_cnt[i + 1] = seen_alpha_cnt[i]
    else:
        j = q.pop()
        if j == -1:
            q.append(i + 1)
            seen_alpha_cnt[i + 1] = seen_alpha_cnt[i]
            continue
        seen_alpha_cnt[i + 1] = seen_alpha_cnt[j]
print("Yes")
        