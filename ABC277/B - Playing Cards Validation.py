N = int(input())
seen = set()
ok = True
for _ in range(N):
    S = input()
    if S in seen or S[0] not in {"H", "D", "C", "S"} or S[1] not in {"A", "2", "3","4","5","6","7","8","9","T","J","Q","K"}:
        ok = False
    seen.add(S)
print("Yes" if ok else "No")