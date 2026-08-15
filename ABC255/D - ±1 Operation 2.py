N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
pref_sum = [0] * len(A)
pref_sum[0] = A[0]
for i in range(1, len(A)):
    pref_sum[i] = pref_sum[i - 1] + A[i]

def nibutan(n:int) -> int:
    left, right = 0, N - 1
    if n >= A[-1]:
        return N - 1
    if n < A[0]:
        return -1
    while right - left > 1:
        mid = (right + left) // 2
        if A[mid] <= n:
            left = mid
        else:
            right = mid
    return left

for _ in range(Q):
    X = int(input())
    idx = nibutan(X)
    if idx == -1:
        print(pref_sum[-1] - X * N)
    elif idx == N - 1:
        print(X * N - pref_sum[-1])
    else:
        print(X * (idx + 1) - pref_sum[idx] + (pref_sum[-1] - pref_sum[idx]) - X * (N - idx - 1))