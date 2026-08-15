from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)
if N % 2:
    l, r = N // 2, N // 2
    cur = 0
    length = 1
    cnt[A[l]] += 1

else:
    l, r = N // 2 - 1, N // 2
    cur = 0 if A[l] == A[r] else 1
    length = 2
    cnt[A[l]] += 1
    cnt[A[r]] += 1
prev = cur

while (l > 0):
    l -= 1
    r += 1
    prev += (length - cnt[A[l]]) + (length - cnt[A[r]]) + (A[l] != A[r])
    cur += prev
    length += 2
    cnt[A[l]] += 1
    cnt[A[r]] += 1
    # print(nxt_prev)

print(cur)