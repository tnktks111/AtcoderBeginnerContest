N = int(input())
cnt = {}
names = []
for _ in range(N):
    s, t = input().split()
    names.append((s, t))
    cnt[s] = cnt.get(s, 0) + 1
    if t != s:
        cnt[t] = cnt.get(t, 0) + 1
for i in range(N):
    if cnt[names[i][0]] > 1 and cnt[names[i][1]] > 1:
        print("No")
        exit()
print("Yes")