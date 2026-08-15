N = int(input())
A = list(map(int, input().split()))
A = set(A)
res = 0
while res in A:
    res += 1
print(res)