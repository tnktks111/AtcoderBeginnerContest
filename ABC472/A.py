S = list(input())

for i in range(len(S)):
    if S[i] != "A":
        S[i] = "."

print("".join(S))
