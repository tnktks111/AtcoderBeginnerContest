N, M = map(int, input().split())
A = list(map(int, input().split()))

res = [0] * M
NumFactors = M
primes = set()

def fprime(n, primes):
	if n == 1:
		return
	i = 2
	while i * i <= n:
		if n % i == 0:
			primes.add(i)
			return (fprime(n // i, primes))
		i += 1
	primes.add(n)
	return

for a in A:
    fprime(a, primes)

for prime in primes:
    i = 1
    while(prime * i <= M):
        if res[prime * i - 1] == 0:
            NumFactors -= 1
            res[prime * i - 1] = 1
        i += 1

print(NumFactors)
for i in range(M):
    if res[i] == 0:
        print(i + 1)
