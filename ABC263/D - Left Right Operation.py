N, L, R = map(int, input().split())
A = list(map(int, input().split()))

L_min = [0] * (N + 1)
R_min = [0] * (N + 1)

for i in range(1, N + 1):
    L_min[i] = min(L_min[i - 1] + A[i - 1], L * i)
for i in range(1, N + 1):
    R_min[N - i] = min(R_min[N - i + 1] + A[N - i], R * i)
res = float("inf")
for i in range(N + 1):
    res = min(L_min[i] + R_min[i], res)
print(res)
 