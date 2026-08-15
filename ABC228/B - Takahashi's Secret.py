N, X = map(int, input().split())
A = list(map(int, input().split()))

seen = set()
cur = X
seen.add(cur)

while True:
    if A[cur - 1] in seen:
        break
    seen.add(A[cur - 1])
    cur = A[cur - 1]
print(len(seen))