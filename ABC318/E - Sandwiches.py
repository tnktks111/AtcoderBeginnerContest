N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))

cnts = [0] * N
left_cnts = [0] * N

for i in range(N):
    cnts[A[i]] += 1

tmp = 0
res = 0

left_cnts[A[0]] += 1

for i in range(1, N - 1):
    prv = A[i - 1]
    cur = A[i]

    if prv != cur:
        tmp += left_cnts[prv] * (cnts[prv] - left_cnts[prv])
        tmp -= left_cnts[cur] * (cnts[cur] - left_cnts[cur])

    res += tmp
    left_cnts[A[i]] += 1

print(res)