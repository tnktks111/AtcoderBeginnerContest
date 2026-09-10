N = int(input())
C = list(map(int, input().split()))

base_i, K = -1, -1
for i in range(9):
    k_cand = N // C[i]
    if k_cand > K:
        base_i, K = i, k_cand

left = N - K * C[base_i]
res = 0

prv_choice = 8
res = []
for k in range(K - 1, -1, -1):
    choice = base_i
    cost = 0
    for i in range(prv_choice, base_i - 1, -1):
        if C[i] - C[base_i] <= left:
            choice = i
            prv_choice = i
            cost = C[i] - C[base_i]
            break
    res.append(str(choice + 1))
    left -= cost
print("".join(res))