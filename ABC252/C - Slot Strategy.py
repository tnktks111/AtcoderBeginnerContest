N = int(input())
times = [[] for _ in range(10)]
res = float("inf")
for _ in range(N):
    S = input()
    for t in range(10):
        num = int(S[t])
        while t in times[num]:
            t += 10
        times[num].append(t)
for i in range(10):
    cur = 0
    cur += max(times[i])
    res = min(res, cur)
print(res)