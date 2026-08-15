N, D = map(int, input().split())
MOD = 998244353

res = 0
for k in range(1, N + 1):
    tmp = 0
    if N - k >= D:
        tmp += 2 ** D
        tmp %= MOD
    if k >= 2 and N + k - 2 >= D:
        if D <= k - 1:
            tmp += 2 ** (D - 1)
            tmp %= MOD
        else:
            tmp += (2 ** (D - 1) - 2 ** (D - k))
            tmp %= MOD
    print(tmp)
    addition = tmp * (2 ** (k - 1)) % MOD
    res = (res + addition) % MOD

print(res)