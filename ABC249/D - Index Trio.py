N = int(input())
A = list(map(int, input().split()))
cnt = {}
res = 0
for i in range(N):
    cnt[A[i]] = cnt.get(A[i], 0) + 1
cnt2 = [(k, v) for k, v in cnt.items()]
cnt2.sort()
num_to_idx = {cnt2[i][0]:i for i in range(len(cnt2))}
Max = cnt2[-1][0]

for i in range(len(cnt2)):
    for j in range(i, len(cnt2)):
        if (k := cnt2[i][0] * cnt2[j][0]) > Max:
            break
        if k in cnt:
            if i == j:
                res += cnt2[i][1] * cnt2[j][1] * cnt2[num_to_idx[k]][1]
            else:
                res += 2 * cnt2[i][1] * cnt2[j][1] * cnt2[num_to_idx[k]][1]
print(res)