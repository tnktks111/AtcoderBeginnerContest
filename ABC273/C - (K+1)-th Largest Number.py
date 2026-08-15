from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
cnt = defaultdict(int)
for a in A:
    cnt[a] += 1

for k in sorted(cnt.keys(), reverse=True):
    print(cnt[k])
for i in range(N - len(cnt.keys())):
    print(0)
