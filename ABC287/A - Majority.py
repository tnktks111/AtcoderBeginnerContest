N = int(input())
res = 0
for _ in range(N):
    if input() == "For":
        res += 1
    else:
        res -= 1
print("Yes" if res > 0 else "No")