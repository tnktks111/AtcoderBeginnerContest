N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = 0
for b in B:
    res += A[b - 1]
print(res)