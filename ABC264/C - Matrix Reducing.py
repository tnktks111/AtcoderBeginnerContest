import itertools
H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]
Hseq = tuple([i for i in range(H1)])
Wseq = tuple([i for i in range(W1)])
H_combs = list(itertools.combinations(Hseq, H2))
W_combs = list(itertools.combinations(Wseq, W2))

for H_comb in H_combs:
    for W_comb in W_combs:
        fail = False
        for h in range(H2):
            if fail:
                break
            for w in range(W2):
                if B[h][w] != A[H_comb[h]][W_comb[w]]:
                    fail = True
                    break
        if not fail:
            print("Yes")
            exit()
print("No")