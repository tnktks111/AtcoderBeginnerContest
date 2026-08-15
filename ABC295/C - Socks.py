N = int(input())
A = list(map(int, input().split()))
res = 0

waiting = set()
for i in range(N):
    if A[i] in waiting:
        waiting.remove(A[i])
        res += 1
    else:
        waiting.add(A[i])
print(res)