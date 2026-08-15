N = int(input())
C = list(map(int, input().split()))

cnt = dict()
for i in range(N):
    cnt[C[i]] = cnt.get(C[i], 0) + 1

print(N - max(cnt.values()))