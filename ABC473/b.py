from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)
for a in A:
    cnt[a] += 1

res = 0
for k, v in cnt.items():
    if v % 2 == 1:
        res += k
print(res)