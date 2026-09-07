from collections import defaultdict

N, K = map(int, input().split())

A = list(map(int, input().split()))
A_acc = [0] * (N + 1)
for i in range(N):
    A_acc[i + 1] = (A_acc[i] + A[i]) % K

last_idx = defaultdict(lambda: -1)
last_use = -1
last_idx[0] = 0

res = 0
# print(A_acc)
for i in range(1, N + 1):
    tmp = A_acc[i]
    if last_idx[tmp] != -1 and last_idx[tmp] >= last_use:
        # print(i, tmp)
        last_use = i
        res += 1
    last_idx[tmp] = i

print(res)