N = int(input())
A = list(map(int, input().split()))
cut_line = [0]
cur = 0
ans = 0
for i in range(len(A)):
    cur = (cur + A[i]) % 360
    cut_line.append(cur)
cut_line.sort()
cut_line.append(360)
for i in range(len(cut_line) - 1):
    ans = max(ans, cut_line[i + 1] - cut_line[i])
print(ans)