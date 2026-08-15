from collections import defaultdict
cnt = defaultdict(int)
N, K = map(int, input().split())
S = input()
for i in range(N - K + 1):
    cnt[S[i:i+K]] += 1
res = max(cnt.values())
resS = []
for key, val in cnt.items():
    if val == res:
        resS.append(key)
resS.sort()
print(res)
print(*resS)