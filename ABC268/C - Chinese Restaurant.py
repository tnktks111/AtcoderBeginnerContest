N = int(input())
P = list(map(int, input().split()))
cuisine_to_idx = {P[i]:i for i in range(N)}

mod = [0] * N
for i in range(N):
    mod[(i - cuisine_to_idx[i]) % N] += 1

res = 0
for i in range(N):
    res = max(res, mod[i] + mod[(i - 1) % N] + mod [(i + 1) % N])
print(res)