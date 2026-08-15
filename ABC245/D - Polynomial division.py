N, M = map(int, input().split())
A, C = list(map(int, input().split()))[::-1], list(map(int, input().split()))[::-1]
B = [0] * (M + 1)
for i in range(M + 1):
    div = C[i] // A[0]
    B[i] = div
    for j in range(N + 1):
        C[i + j] -= div * A[j]
print(*B[::-1])