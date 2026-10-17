N = int(input())
A = list(map(int, input().split()))

res = 0
for i in range(N):
    if i % 2 == 0:
        res += A[i]

print(res)