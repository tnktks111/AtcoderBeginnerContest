S = input()
res = 0
for i in range(len(S)):
    res += (ord(S[i]) - ord("A") + 1) * (26 ** (len(S) - 1 - i))
print(res)