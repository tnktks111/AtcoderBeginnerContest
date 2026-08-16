from collections import defaultdict
N = int(input())
cnt = defaultdict(int)
for _ in range(N):
    cnt[input().lower()] += 1

print(max(cnt.values()))