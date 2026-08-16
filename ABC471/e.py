
N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353

sum_nums = 0
for a in A:
    sum_nums = (sum_nums + a) % MOD

sum_squares = 0
for a in A:
    sum_squares = (sum_squares + pow(a, 2, MOD)) % MOD

if K == 1:
    print(sum_squares)
    exit()

# n-1Ck-1 = (n-1)! / (k-1)! * (n-k)!
# n-2Ck-2 = (n-2)! / (k-2)! * (n-k)!
# fact[n - 1], fact[n - 2], ifact[k - 1], ifact[k - 2], ifact[n - k]が必要

fact_n_1 = 1
fact_n_2 = 1
fact_k_1 = 1
fact_k_2 = 1
fact_n_k = 1

tmp = 1
for i in range(1, N + 1):
    tmp = (tmp * i) % MOD
    if i == N - K:
        fact_n_k = tmp
    if i == K - 2:
        fact_k_2 = tmp
    if i == K - 1:
        fact_k_1 = tmp
    if i == N - 2:
        fact_n_2 = tmp
    if i == N - 1:
        fact_n_1 = tmp

ifact_k_1 = pow(fact_k_1, MOD - 2, MOD)
ifact_k_2 = pow(fact_k_2, MOD - 2, MOD)
ifact_n_k = pow(fact_n_k, MOD - 2, MOD)

# print(fact_n_1, fact_n_2, fact_k_1, fact_k_2, fact_n_k)

n1Ck1 = fact_n_1 * ifact_k_1 * ifact_n_k
n2Ck2 = fact_n_2 * ifact_k_2 * ifact_n_k

res1 = n1Ck1 * sum_squares % MOD

res2 = 0
for a in A:
    others = (sum_nums - a) % MOD
    corr = a * others % MOD
    term = n2Ck2 * corr % MOD
    res2 = (res2 + term) % MOD

print((res1 + res2) % MOD)
    