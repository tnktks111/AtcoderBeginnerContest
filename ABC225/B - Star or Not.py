N = int(input())
cnt = {}
for _ in range(N - 1):
    a, b = map(int, input().split())
    cnt[a] = cnt.get(a, 0) + 1
    cnt[b] = cnt.get(b, 0) + 1

if max(cnt.values()) == N - 1 and len(cnt) == N:
    print("Yes")
else:
    print("No")