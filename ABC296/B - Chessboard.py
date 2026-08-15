found = False
res = []
for r in range(8):
    S = input()
    if found:
        continue
    for c in range(8):
        if S[c] == "*":
            found = True
            res.append((r, c))
            break
r, c = res[0]
col = "abcdefgh"
row = "87654321"
print(f"{col[c]}{row[r]}")