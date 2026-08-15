A, X, M = map(int, input().split())
def mod_pow(a:int, n:int, mod:int):
    ans = 1
    a %= mod
    while n:
        if n & 1:
            ans = (ans * a) % mod
        a = (a * a) % mod
        n >>= 1
    return ans

if A == 1:
    print(X % M)
else:
    print(((mod_pow(A, X, M * (A - 1)) - 1) // (A - 1)) % M)