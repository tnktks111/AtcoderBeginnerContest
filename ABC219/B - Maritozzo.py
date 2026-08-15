S = [input() for _ in range(3)]
T = input()
res = []
for i in range(len(T)):
    res.append(S[int(T[i]) - 1])
print("".join(res))

