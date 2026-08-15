N = int(input())
A = list(map(int, input().split()))
post_sum = [0] * N
post_sum[-1] = A[-1]
res = int(post_sum[-1] > 3)
for i in range(N - 2, -1, -1):
    post_sum[i] = post_sum[i + 1] + A[i]
    if post_sum[i] > 3:
        res += 1
print(res)