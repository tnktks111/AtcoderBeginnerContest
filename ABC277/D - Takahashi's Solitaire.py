from collections import defaultdict, Counter
N, M = map(int, input().split())
A = list(map(int, input().split()))
kv = sorted([(k, v) for k, v in Counter(A).items()])

start = 0
res = sum(A)
first = True
while (kv[start][0] - 1) % M == kv[start - 1][0]:
    start = (start + 1) % len(kv)
    if not first and start == 0:
        print(0)
        exit()
    first = False
        
kv = kv[start:] + kv[:start]
prev = kv[0][0] % M - 1
max_deletion = 0
curr_deletion = 0
# print(kv)
for i in range(len(kv)):
    if (kv[i][0] - (prev + 1)) % M > 0:
        max_deletion = max(max_deletion, curr_deletion)
        curr_deletion = 0
    prev = kv[i][0] % M
    curr_deletion += kv[i][0] * kv[i][1]
max_deletion = max(max_deletion, curr_deletion)
print(res - max_deletion)