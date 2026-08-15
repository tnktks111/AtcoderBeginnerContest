MOD = 998244353
N = list(map(int, input().split()))
print((N[0] * N[1] * N[2] - N[3] * N[4] * N[5]) % MOD)