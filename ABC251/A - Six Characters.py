S = input()
res = []
for _ in range(6 // len(S)):
    res.append(S)
print("".join(res))