import bisect
N, A, B = map(int, input().split())
S = input()

l = 0
cumcnt = []
A_sum = [0]
B_sum = [0]

cnt = [0, 0]
for i in range(N):
    if S[i] == "a":
        cnt[0] += 1
    else:
        cnt[1] += 1
    A_sum.append(cnt[0])
    B_sum.append(cnt[1])

res = 0
# print(A_sum)
# print(B_sum)
for i in range(N):
    a = bisect.bisect_right(A_sum, A_sum[i + 1] - A)
    b = bisect.bisect_right(B_sum, B_sum[i + 1] - B)
    res += max(a - b, 0)
    # print(f"at i = {i}, res = {res}, a = {a}, b = {b}")

print(res)