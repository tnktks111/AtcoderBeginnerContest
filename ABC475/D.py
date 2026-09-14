import math

S = input()
N = len(S)

def primes(x):
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0 # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > math.sqrt(x): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0
    
    return [prime for prime in primes if prime != 0]


inf = 10 ** (N - 1)
sup = 10 ** N

res = primes(sup)

def calc_hash(str):
    res = 0
    nxt = 1
    c2num = dict()
    for c in str:
        if c not in c2num:
            c2num[c] = nxt
            nxt += 1
        res *= 10
        res += c2num[c]
    return res

target = calc_hash(S)

for n in res:
    if n < inf:
        continue
    if target == calc_hash(str(n)):
        print(n)
        exit()
print(-1)
