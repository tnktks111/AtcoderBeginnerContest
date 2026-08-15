from collections import Counter
H, W = map(int, input().split())
C = [input() for _ in range(H)]
C_t = list(zip(*C))
res = [Counter(col)["#"] for col in C_t]
print(*res)