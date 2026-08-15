N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

most_del = max(A)
for i in range(K):
    if A[B[i] - 1] == most_del:
        print("Yes")
        exit()
print("No")