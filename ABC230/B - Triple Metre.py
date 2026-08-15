S = input()

reps = ["oxx", "xxo", "xox"]

if len(S) == 1:
    print("Yes")
    exit()

if len(S) == 2:
    if S != "oo":
        print("Yes")
    else:
        print("No")
    exit()

if len(S) == 3:
    if S in reps:
        print("Yes")
    else:
        print("No")
    exit()

def is_substring(s1, s2):
    if len(s1) == 1:
        return (s1 == s2[0])
    if len(s1) == 2:
        return (s1 == s2[0:2])
    return (s1 == s2)

rep = S[0:3]
if rep not in reps:
    print("No")
    exit()

for i in range(1, len(S) // 3 + 1):
    if not is_substring(S[i * 3 : min(i * 3 + 3, len(S))], rep):
        print("No")
        exit()
print("Yes")
