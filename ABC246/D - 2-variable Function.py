N = int(input())
res = float("inf")

j = 10 ** 6
for i in range(10 ** 6 + 1):
    while (i + j) * (i ** 2 + j ** 2) >= N and j >= 0:
        res = min(res, (i + j) * (i ** 2 + j ** 2))
        j -= 1
print(res)