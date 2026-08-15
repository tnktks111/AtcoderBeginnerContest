N, M = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
for a in A:
    if S - a == M:
        print("Yes")
        exit()
print("No")