T = int(input())
for _ in range(T):
    ok = False
    a, s = map(int, input().split())
    if s - (a << 1) >= 0 and (s - (a << 1)) & a == 0:
        print("Yes")
    else:
        print("No")