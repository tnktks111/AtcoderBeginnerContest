N, P = map(int, input().split())
A = list(map(int, input().split()))
res = 0
for a in A:
    if a < P:
        res += 1
print(res)