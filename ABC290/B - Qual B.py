N, K = map(int, input().split())
S = input()
res = []
for c in S:
    if K == 0:
        break
    if c == "o":
        K -= 1
        res.append("o")
    else:
        res.append("x")
for _ in range(N - len(res)):
    res.append("x")
print("".join(res))