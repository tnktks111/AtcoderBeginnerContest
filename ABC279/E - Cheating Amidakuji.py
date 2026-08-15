N, M = map(int, input().split())
A = list(map(int, input().split()))

pre = 0
post = [i for i in range(N)]

for i in range(M - 1, -1, -1):
    post[A[i] - 1], post[A[i]] = post[A[i]], post[A[i] - 1]

for i in range(M):
    post[A[i] - 1], post[A[i]] = post[A[i]], post[A[i] - 1]
    print(post[pre] + 1)
    if pre == A[i] - 1:
        pre = A[i]
    elif pre == A[i]:
        pre = A[i] - 1