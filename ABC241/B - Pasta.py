N, M = map(int, input().split())
A, B = list(map(int, input().split())), list(map(int, input().split()))
cnt_A = {}
for i in range(N):
    cnt_A[A[i]] = cnt_A.get(A[i], 0) + 1
ok = True
for i in range(M):
    if not B[i] in cnt_A or cnt_A[B[i]] == 0:
        ok = False
        break
    cnt_A[B[i]] -= 1
print("Yes" if ok else "No")