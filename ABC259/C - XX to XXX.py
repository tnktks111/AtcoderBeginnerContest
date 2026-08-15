S, T = input(), input()

def str_encoder(s:str) -> str:
    i = 0
    cnt = 1
    res = []
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            res.append((s[i], cnt))
            cnt = 1
        i += 1
    res.append((s[-1], cnt))
    return res

S_encoded = str_encoder(S)
T_encoded = str_encoder(T)

if len(S_encoded) != len(T_encoded):
    print("No")
    exit()

ok = True
for i in range(len(S_encoded)):
    if S_encoded[i][0] != T_encoded[i][0]:
        ok = False
        break
    if S_encoded[i][1] == 1 and T_encoded[i][1] > 1:
        ok = False
        break
    if S_encoded[i][1] > T_encoded[i][1]:
        ok = False
        break
print("Yes" if ok else "No")
