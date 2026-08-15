T = int(input())

def gcd(a, b) -> int:
    if a > b:
        return gcd(b, a)
    if b % a == 0:
        return a
    return gcd(a, b % a)

def lcm(a, b) -> int:
    m = gcd(a, b)
    return a * b // m

for _ in range(T):
    N, D, K = map(int, input().split())
    m = gcd(N, D)
    if m == 1:
        print(D * (K - 1) % N)
    else:
        cycle = N // m
        q, mod = divmod(K - 1, cycle)
        print((q + mod * D) % N)
