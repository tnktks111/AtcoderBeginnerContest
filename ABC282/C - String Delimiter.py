N = int(input())
S = list(input())
in_parentheses = False

for i in range(N):
    if S[i] == "\"":
        in_parentheses = not in_parentheses
    elif S[i] == "," and not in_parentheses:
        S[i] = "."
print("".join(S))