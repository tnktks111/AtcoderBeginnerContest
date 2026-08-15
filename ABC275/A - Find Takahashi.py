N = int(input())
H = list(map(int, input().split()))

res = (-1, -1)
for i in range(N):
    if H[i] > res[0]:
        res = (H[i], i)
print(res[1] + 1)
    