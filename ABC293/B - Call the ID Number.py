N = int(input())
A = list(map(int, input().split()))

called = [False] * N
for i in range(N):
    if called[i] == False:
        called[A[i] - 1] = True
res = [i+1 for i in range(N) if called[i] == False]
print(len(res))
print(*res)
