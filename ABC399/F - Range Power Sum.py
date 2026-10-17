import math

MOD = 998244353
N, K = map(int, input().split())
A = list(map(int, input().split()))

acc_corr = [[0] * (K + 1) for _ in range(N + 1)]

facts = [1] * (K + 1)
ifacts = [1] * (K + 1)

for i in range(1, K + 1):
    facts[i] = (facts[i - 1] * i) % MOD

ifacts[-1] = pow(facts[-1], MOD - 2, MOD)
for i in range(K, 0, -1):
    ifacts[i - 1] = (ifacts[i] * i) % MOD

def combination(n:int, k:int):
    return (facts[n] * ifacts[n - k] * ifacts[k]) % MOD

res = 0
for i in range(1, N + 1):
    for m in range(K + 1):
        acc_corr[i][m] = pow(A[i - 1], m, MOD)
        for n in range(m + 1):
            acc_corr[i][m] += (combination(m, n) * acc_corr[i - 1][n] * pow(A[i - 1], m - n, MOD)) % MOD
            acc_corr[i][m] %= MOD
    res += acc_corr[i][K]
    res %= MOD

# print(*acc_corr, sep="\n")

print(res)
