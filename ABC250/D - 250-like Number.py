N = int(input())
def Eratosthenes(n:int):
    isprime = [True] * (n + 1)
    isprime[0] = isprime[1] = False
    for p in range(2, n + 1):
        if not isprime[p]:
            continue
        q = p * 2
        while q <= n:
            isprime[q] = False
            q += p
    res = [i for i in range(n + 1) if isprime[i]]
    return res
isp = Eratosthenes(min(N, 10**6))
res = 0
for i in range(len(isp) - 1):
    for j in range(i + 1, len(isp)):
        if isp[i] * (isp[j] ** 3) > N:
            break
        res += 1
print(res)