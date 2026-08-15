from collections import defaultdict
N, M, T = map(int, input().split())
A = [0] + list(map(int, input().split()))
bonus = defaultdict(int)
for _ in range(M):
    x, y = map(int, input().split())
    bonus[x] = y

for i in range(1, N):
    T += bonus[i]
    if T - A[i] <= 0:
        print("No")
        exit()
    T -= A[i]

print("Yes")