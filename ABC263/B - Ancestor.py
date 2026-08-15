N = int(input())
P = list(map(int, input().split()))

cur = N
res = 0
while cur != 1:
    cur = P[cur - 2]
    res += 1
print(res)