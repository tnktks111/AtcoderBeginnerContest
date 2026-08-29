N, M, K = map(int, input().split())
A = list(map(int, input().split()))
eat = [False] * N

tmp = 0
for i in range(N):
    if i >= M:
        if eat[i - M]:
            tmp -= A[i - M]
    if tmp + A[i] <= K:
        eat[i] = True
        tmp += A[i]

for i in range(N):
    if eat[i]:
        print("Yes")
    else:
        print("No")
