N = int(input())
A = list(map(int, input().split()))
cnt = [4] * N
target = set(list(range(1, N + 1)))

for i in range(4 * N - 1):
    cnt[A[i] - 1] -= 1
    if cnt[A[i] - 1] == 0:
        target.remove(A[i])
print(list(target)[0])