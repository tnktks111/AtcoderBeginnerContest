from collections import Counter
H, W = map(int, input().split())
S = list(input() for _ in range(H))
c = Counter("".join(S))
print(c["#"])