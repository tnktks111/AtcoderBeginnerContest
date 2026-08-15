from collections import defaultdict
import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

S = input()
pattern = defaultdict(int)
cur = 0

pattern[0] += 1
for i in range(len(S)):
    cur ^= 1 << int(S[i])
    pattern[cur] += 1

res = 0
for cnt in pattern.values():
    if cnt >= 2:
        res += comb(cnt, 2)
print(res)