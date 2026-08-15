S = input()

push_00 = False
res = 0
for i in range(len(S)):
    if push_00 == True:
        push_00 = False
        continue
    if i + 1 < len(S) and S[i] == "0" and S[i + 1] == "0":
        push_00 = True
    res += 1
print(res)