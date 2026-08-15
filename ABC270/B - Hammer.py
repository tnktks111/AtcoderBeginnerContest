X, Y, Z = map(int, input().split())

if X < 0:
    X *= -1
    Y *= -1
    Z *= -1

if 0 < Y < X:
    if Y < Z:
        print(-1)
        exit()
    else:
        print(X - min(2 * Z, 0))
        exit()
else:
    print(X)
