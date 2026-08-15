from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
cnt = defaultdict(int)
over_two = []
for a in A:
    cnt[a] += 1
    if cnt[a] == 2:
        over_two.append(a)

res = 0
for a in over_two:
    res += (cnt[a] * (cnt[a] - 1) // 2) * (N - cnt[a])
print(res)