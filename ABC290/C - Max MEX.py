N, K = map(int, input().split())
A = list(map(int, input().split()))

A_set = sorted(list(set(A)))
for i in range(K):
    if i >= len(A_set) or A_set[i] != i:
        print(i)
        exit()
print(K)