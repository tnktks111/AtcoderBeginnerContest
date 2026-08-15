W = int(input())
res = []
for i in range(100):
    res.append(i + 1)
for i in range(100):
    res.append((i + 1) * 100)
for i in range(100):
    res.append((i + 1) * 10000)

print(len(res))
print(*res)