N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

def is_on_Sameline(x1, y1, x2, y2, x3, y3):
    if (x1 == x2 == x3):
        return True
    elif (x1 == x2 or x2 == x3 or x3 == x1):
        return False
    return (y1 - y2) / (x1 - x2) == (y2 - y3) / (x2 - x3)

count = 0

for i in range(N - 2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if not is_on_Sameline(xy[i][0], xy[i][1], xy[j][0], xy[j][1], xy[k][0], xy[k][1]):
                count += 1
print(count)