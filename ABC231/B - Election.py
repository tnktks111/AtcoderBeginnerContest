N = int(input())
cnt = {}
for _ in range(N):
    S = input()
    cnt[S] = cnt.get(S, 0) + 1
print(max(cnt, key = cnt.get))