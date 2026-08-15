N = int(input())
S = input()

res = 0
for i in range(N):
    if S[i] == "o":
        continue
    if i != 0 and S[i - 1] == "o":
        continue
    if i != N - 1 and S[i + 1] == "o":
        continue
    res += 1

print(res)