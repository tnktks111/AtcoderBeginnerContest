A = list(map(int, input().split()))
cnt = dict()
for i in range(5):
    cnt[A[i]] = cnt.get(A[i], 0) + 1
kv_pair = list(cnt.values())
if len(kv_pair) == 2 and (kv_pair[0] == 2 and kv_pair[1] == 3) or (kv_pair[0] == 3 and kv_pair[1] == 2):
    print("Yes")
else:
    print("No")