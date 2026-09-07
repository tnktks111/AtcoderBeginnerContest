from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnts = defaultdict(int)
max_cnt = -1
for a in A:
    cnts[a] += 1
    max_cnt = max(max_cnt, cnts[a])

res = 0
for i in range(1, K + 1):
    if cnts[i] == max_cnt or cnts[i] + 1 == max_cnt:
        res += 1

print(res)

