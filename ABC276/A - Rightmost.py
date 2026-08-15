S = input()
res = -1
for i, c in enumerate(S):
    if c == "a":
        res = i + 1
print(res)