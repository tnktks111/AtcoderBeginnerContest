P = list(map(int, input().split()))
res = []
for i in range(26):
    res.append(chr(P[i] + 96))
print("".join(res))