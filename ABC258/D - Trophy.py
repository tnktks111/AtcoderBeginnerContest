N, X = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
prereq = [0] * N
prereq[0] = AB[0][0]
for i in range(1, N):
    prereq[i] = prereq[i - 1] + AB[i - 1][1] + AB[i][0]
res = float("inf")
for i in range(N):
    if i >= X:
        break
    res = min(prereq[i] + AB[i][1] * (X - i), res)
print(res)