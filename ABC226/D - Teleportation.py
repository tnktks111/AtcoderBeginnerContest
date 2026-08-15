def gcd(a:int, b:int):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
magics = set()

for i in range(N - 1):
    for j in range(i + 1, N):
        vec1 = [xy[j][0] - xy[i][0], xy[j][1] - xy[i][1]]
        m = gcd(vec1[0], vec1[1])
        vec1 = [vec1[0] / m, vec1[1] / m]
        vec2 = [-vec1[0], -vec1[1]]
        magics.add(tuple(vec1))
        magics.add(tuple(vec2))
print(len(magics))