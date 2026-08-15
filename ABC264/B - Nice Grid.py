R, C = map(int, input().split())

x, y = C, R
x -= 8
y = 8 - R

if max(abs(x), abs(y)) % 2 == 0:
    print("white")
else:
    print("black")