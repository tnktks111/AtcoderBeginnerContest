N = int(input())

res = 0
for _ in range(N):
    a, b, s = input().split()
    a = int(a)
    b = int(b)
    if s == "keep":
        res += b - a

print(res)