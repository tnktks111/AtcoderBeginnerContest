N = int(input())
isprime = [True] * (10**6 + 2)
isprime[0] = False
isprime[1] = False
primes = []
for i in range(2, len(isprime)):
    if isprime[i] == True:
        primes.append(i)
        for j in range(2, len(isprime)):
            if i * j >= len(isprime):
                break
            isprime[i * j] = False

res = 0
for i in range(len(primes) - 2):
    if primes[i] ** 2 * primes[i+1] * primes[i+2] ** 2 > N:
        break
    for j in range(i+1, len(primes) - 1):
        if primes[i] ** 2 * primes[j] * primes[j+1] ** 2 > N:
            break
        for k in range(j+1, len(primes)):
            if primes[i] ** 2 * primes[j] * primes[k] ** 2 > N:
                break
            res += 1
print(res)
