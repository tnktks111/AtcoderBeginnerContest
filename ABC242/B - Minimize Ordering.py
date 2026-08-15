S = input()
cnt = [0] * 26
res = []
for i in range(len(S)):
    cnt[ord(S[i]) - 97] += 1
for i in range(26):
    for _ in range(cnt[i]):
        res.append(chr(97 + i))
print("".join(res))