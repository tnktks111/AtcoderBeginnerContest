import math

X = input()
X_int = int(X)
k = len(X)

if k == 1:
    print(X)
    exit()

if k > 10:
    base = (pow(10, k) - 1) // 9
    if X_int <= base * int(X[0]):
        print(base * int(X[0]))
    else:
        print(base * (int(X[0]) + 1))
    exit()

start = int(X[0])
step = k - 1

d_min = math.ceil((0 - start) / step)
d_max = math.floor((9 - start) / step)
for d in range(d_min, d_max + 1):
    num = 0
    cur = start
    for i in range(k):
        num += cur * pow(10, k - 1 - i)
        cur = cur + d
    if num >= X_int:
        print(num)
        exit()

start = int(X[0]) + 1
d_min = math.ceil((0 - start) / step)
num = 0
cur = start
for i in range(k):
    num += cur * pow(10, k - 1 - i)
    cur = cur + d_min
if num >= X_int:
    print(num)
    exit()