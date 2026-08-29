N = int(input())
L = list(map(int, input().split()))

total = sum(L)

res = float("inf")
for i in range(N - 1):
    section = sum(L[:i + 1])
    res = min(res, abs(section - (total - section)))
print(res)