H, W = map(int, input().split())
R, C = map(int, input().split())

res = 4
if H == 1:
    res -= 1
if W == 1:
    res -= 1
if R == 1 or R == H:
    res -= 1
if C == 1 or C == W:
    res -= 1
print(res)
