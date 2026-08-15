S = input()
if len(S) != 8:
    print("No")
    exit()
if not S[0].isupper() or not S[-1].isupper():
    print("No")
    exit()
if not S[1:-1].isdigit():
    print("No")
    exit()
print("Yes" if 100000 <= int(S[1:-1]) <= 999999 else "No")