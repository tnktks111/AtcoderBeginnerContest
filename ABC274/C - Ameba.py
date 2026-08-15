N = int(input())
A = list(map(int, input().split()))
decendents = [0] * (2 * N + 1)
for i in range(N):
    decendents[2 * i + 1] = decendents[A[i] - 1] + 1
    decendents[2 * i + 2] = decendents[A[i] - 1] + 1
print(*decendents, sep="\n")