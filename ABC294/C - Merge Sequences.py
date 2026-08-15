N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_i, b_i = 0, 0
cur = 1

while a_i < N and b_i < M:
    if A[a_i] < B[b_i]:
        A[a_i] = cur
        a_i += 1
    else:
        B[b_i] = cur
        b_i += 1
    cur += 1

for i in range(a_i, N):
    A[i] = cur
    cur += 1

for i in range(b_i, M):
    B[i] = cur
    cur += 1

print(*A)
print(*B)