
N, K, T = map(int, input().split())
A = list(map(int, input().split()))
A.append(T)
A.sort()

last = 0
push_cnt = 0
for i in range(len(A)):
    if A[i] > T:
        break
    while last < A[i]:
        # print(last, A[i])
        push_cnt += 1
        last += K
    last = A[i] + K

print(push_cnt)