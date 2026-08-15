xy = [list(map(int, input().split())) for _ in range(3)]
res = [0, 0]
if xy[0][0] == xy[1][0]:
    res[0] = xy[2][0]
if xy[1][0] == xy[2][0]:
    res[0] = xy[0][0]
if xy[2][0] == xy[0][0]:
    res[0] = xy[1][0]
if xy[0][1] == xy[1][1]:
    res[1] = xy[2][1]
if xy[1][1] == xy[2][1]:
    res[1] = xy[0][1]
if xy[2][1] == xy[0][1]:
    res[1] = xy[1][1]
print(*res)