MOD = 998244353

N, K, M = map(int, input().split())

n = pow(K, N, MOD - 1)
if M % MOD == 0:
    if K == 0 and N > 0:
        print(1)
    else:
        print(0)
else:
    print(pow(M, pow(K, N, MOD - 1), MOD))