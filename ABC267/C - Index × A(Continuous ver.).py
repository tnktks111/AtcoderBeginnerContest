N, M = map(int, input().split())
A = list(map(int, input().split()))


cur_plain_sum = sum(A[:M])
cur_sum = 0
for i in range(M):
    cur_sum += (i + 1) * A[i]
res = cur_sum
for i in range(1, N - M + 1):
    cur_sum -= cur_plain_sum
    cur_sum += M * A[i + M - 1]
    res = max(res, cur_sum)
    cur_plain_sum -= A[i - 1]
    cur_plain_sum += A[i + M - 1]
print(res)