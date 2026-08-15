from collections import defaultdict
N = int(input())
cnt = defaultdict(int)
for _ in range(N):
    S = input()
    cur = cnt[S]
    if cur == 0:
        print(S)
    else:
        print(f"{S}({cur})")
    cnt[S] += 1
