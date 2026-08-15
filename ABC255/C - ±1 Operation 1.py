X, A, D, N = map(int, input().split())

start, end = A, A + D * (N - 1)
if start > end:
    start, end = end, start
if start >= X:
    print(start - X)
elif end <= X:
    print(X - end)
elif D == 0:
    print(X - A)
else:
    print(min(abs(X - start) % abs(D), abs(D) - abs(X - start) % abs(D)))
