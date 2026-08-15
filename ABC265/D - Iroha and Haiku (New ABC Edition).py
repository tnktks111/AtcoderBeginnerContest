N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

P_rec = [-1] * N
Q_rec = [-1] * N
R_rec = [-1] * N

cur = 0
r = 0
for l in range(N):
    while cur < P and r < N:
        cur += A[r]
        r += 1
    if cur == P:
        P_rec[l] = r
    cur -= A[l]

cur = 0
r = 0
for l in range(N):
    while cur < Q and r < N:
        cur += A[r]
        r += 1
    if cur == Q:
        Q_rec[l] = r
    cur -= A[l]

cur = 0
r = 0
for l in range(N):
    while cur < R and r < N:
        cur += A[r]
        r += 1
    if cur == R:
        R_rec[l] = r
    cur -= A[l]

for i in range(N):
    if 0 < P_rec[i] < N and 0 < Q_rec[P_rec[i]] < N and R_rec[Q_rec[P_rec[i]]] > 0:
        print("Yes")
        exit()
print("No")