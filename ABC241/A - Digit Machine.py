A = list(map(int, input().split()))
nxt = 0
for _ in range(3):
    nxt = A[nxt]
print(nxt)