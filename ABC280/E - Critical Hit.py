import math

MOD = 998244353
N, P = map(int, input().split())
INV_100 = pow(100, MOD - 2, MOD)
p, q = P * INV_100 % MOD, (100 - P) * INV_100 % MOD
factorial_MOD = [1] * (N + 1)
p_square = [1] * (N + 1)
q_square = [1] * (N + 1)

for i in range(1, N + 1):
    factorial_MOD[i] = factorial_MOD[i - 1] * i % MOD
    p_square[i] = p_square[i - 1] * p % MOD
    q_square[i] = q_square[i - 1] * q % MOD

def comb(a:int, b:int):
    inv_1 = pow(factorial_MOD[b], MOD - 2, MOD)
    inv_2 = pow(factorial_MOD[a - b], MOD - 2, MOD)
    return factorial_MOD[a] * inv_1 * inv_2 % MOD

res = 0
for k in range(math.ceil(N / 2), N + 1):
    res += k * comb(k, N - k) * p_square[N - k] * q_square[2 * k - N]
    if k >= (N + 1) / 2:
        res += k * comb(k - 1, N - k) * p_square[N - k + 1] * q_square[2 * k - N - 1]
    res %= MOD
print(res)