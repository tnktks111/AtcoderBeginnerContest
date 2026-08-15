MOD = 998244353

N = int(input())
A = list(map(int, input().split()))
inv = [0] * (N + 1)
inv[1] = 1

inv_sum = 1
for i in range(2, N + 1):
    inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
    inv_sum = (inv_sum + inv[i]) % MOD

N_sum = 0    
for i in range(N):
    N_sum = (N_sum + A[i]) % MOD

inv_accumulation = [0] * ((N + 1) // 2)
inv_accumulation[0] = inv_sum
accumulation = [0] * ((N + 1) // 2)
accumulation[0] = N_sum

for i in range(1, len(inv_accumulation)):
    inv_accumulation[i] = (inv_accumulation[i - 1] - ((inv[i] + inv[-i]) % MOD)) % MOD
    accumulation[i] = (accumulation[i - 1] - (A[i - 1] + A[-i]) % MOD) % MOD

res = 0
for i in range(len(inv_accumulation)):
    res += accumulation[i] * inv_accumulation[i]
    res %= MOD

print(res)