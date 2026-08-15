import bisect
N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))
H.sort()
B.sort()
tmp = 0
res = 0
for i in range(M):
    if tmp < N and B[i] < H[tmp]:
        continue
    if tmp == N:
        break
    tmp += 1
    res += 1
# print(res)
print("Yes" if K <= res else "No")