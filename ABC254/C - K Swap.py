N, K = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(A)
ok = True
for i in range(K):
    C, D = [], []
    j = 0
    while i + K * j < N:
        C.append(A[i + K * j])
        j += 1
    j = 0
    while i + K * j < N:
        D.append(B[i + K * j])
        j += 1
    C.sort()
    if C != D:
        ok = False
        break
print("Yes" if ok else "No")