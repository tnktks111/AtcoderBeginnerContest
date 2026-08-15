S, T = list(input().split()), list(input().split())
diff = 0
for i in range(3):
    if S[i] != T[i]:
        diff += 1
if diff == 0 or diff == 3:
    print("Yes")
else:
    print("No")