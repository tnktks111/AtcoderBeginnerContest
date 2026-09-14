S = input()
res = []
for i in range(len(S)):
    res.append(S[i])
    if i != len(S) - 1:
        res.append("o")

print("".join(res))