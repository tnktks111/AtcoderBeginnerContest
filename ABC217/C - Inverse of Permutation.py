N = int(input())
P = list(map(int, input().split()))
res = [0] * N
for i in range(N):
    res[P[i] - 1] = str(i + 1)
print(' '.join(res))