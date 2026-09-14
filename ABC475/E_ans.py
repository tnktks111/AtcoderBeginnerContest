N, M, K = map(int, input().split())
T = input()

S = []
for _ in range(N):
    s = input()
    S.append(s)

Q = int(input())
for _ in range(Q):
    i, j = map(lambda x: int(x) - 1, input().split())
    prv = S[i]
    new_char = "o" if prv[j] == "x" else "x"
    nxt = S[i][:j] + new_char + S[i][j + 1:]
    S[i] = nxt
    print(S)

    tmp = 0

    remain = range(N)
    decided = False
    for k in range(K):
        if decided:
            break
        seikai = []
        machigai = []
        for j in remain:
            if S[j][k] == T[k]:
                seikai.append(j)
            else:
                machigai.append(j)
        is_seikai = (S[i][k] == T[k])

        if tmp + len(seikai) <= K:
            tmp += len(seikai)
            remain = machigai
            if is_seikai:
                print("Yes")
                decided = True
        else:
            remain = seikai

    if not decided:
        print("No")
    