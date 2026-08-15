from bisect import bisect_left, bisect_right

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_adjsum = [(A[i] + A[i + 1]) % M for i in range(N - 1)]
base = [0] * N

for i in range(N - 1):
    base[i + 1] = (B[i] - A_adjsum[i]) % M
    if i != N - 2:
        A_adjsum[i + 1] = (A_adjsum[i + 1] + base[i + 1]) % M
first_sum = sum(base)

evens = []
odds = []
even_cnts = dict()
odd_cnts = dict()

for i in range(N):
    if i % 2 == 0:
        even_cnts[base[i]] = even_cnts.get(base[i], 0) + 1
    else:
        odd_cnts[base[i]] = odd_cnts.get(base[i], 0) + 1

evens = list(even_cnts.keys())
odds = list(odd_cnts.keys())
evens.sort()
odds.sort()
even_higher = dict()
odd_lower = dict()
prv = -1
for even in evens[::-1]:
    if prv != -1:
        even_higher[even] = even_cnts[even] + even_higher[prv]
    else:
        even_higher[even] = even_cnts[even]
    prv = even

prv = -1
for odd in odds:
    if prv != -1:
        odd_lower[odd] = odd_cnts[odd] + odd_lower[prv]
    else:
        odd_lower[odd] = odd_cnts[odd]
    prv = odd

res = first_sum
for i in range(N):
    if base[i] == 0:
        continue
    if N % 2 == 0:
        tmp = 0
    else:
        if i % 2 == 0:
            tmp = (M - base[i]) % M
        else:
            tmp = base[i]
    if i % 2 == 0:
        k = bisect_left(evens, base[i])
        if k != len(evens):
            tmp -= even_higher[evens[k]] * M
        k = bisect_left(odds, (M - base[i]) % M) - 1
        if k >= 0:
            tmp += odd_lower[odds[k]] * M
    else:
        k = bisect_left(evens, (M - base[i]) % M)
        if k != len(evens):
            tmp -= even_higher[evens[k]] * M
        k = bisect_left(odds, base[i]) - 1
        if k >= 0:
            tmp += odd_lower[odds[k]] * M
    res = min(res, first_sum + tmp)

print(res)

