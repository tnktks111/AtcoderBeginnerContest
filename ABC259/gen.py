from random import randint

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
L = len(primes)

N = 3
print(N)
for i in range(N):
    M = randint(1, 5)
    print(M)
    for _ in range(M):
        p = primes[randint(0, L - 1)]
        e = randint(1, 5)
        print(p, e)

