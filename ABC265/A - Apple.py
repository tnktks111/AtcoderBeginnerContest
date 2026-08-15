X, Y, N = map(int, input().split())
if X * 3 > Y:
    print((N // 3) * Y + (N % 3) * X)
else:
    print(X * N)