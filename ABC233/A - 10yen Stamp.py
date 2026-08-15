X, Y = map(int, input().split())
if Y <= X:
    print(0)
else:
    remain = Y - X
    if remain % 10 == 0:
        print(remain // 10)
    else:
        print(remain // 10 + 1)