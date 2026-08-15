N = int(input())
S = list(map(int, input().split()))
maxS = max(S)
max_long = int(maxS - 3 / 7) + 1
memo = set()
for a in range(1, max_long + 1):
    for b in range(1, max_long + 1):
        memo.add(4 * a * b + 3 * a + 3 * b)
res = 0
for s in S:
    res += (s not in memo)
print(res)