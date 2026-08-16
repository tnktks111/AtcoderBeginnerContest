from sortedcontainers import SortedList

N = int(input())
A = list(map(int, input().split()))

cookies = SortedList(A)

cur = 0
res = 0
for _ in range(N):
    i = cookies.bisect_left(cur)
    if i == len(cookies):
        res += abs(cur - cookies[-1])
        cur = cookies[-1]
        cookies.remove(cur)
    # すべての要素が相異なるのでiとi-1を比較
    else:
        if i == 0:
            res += abs(cur - cookies[0])
            cur = cookies[0]
            cookies.remove(cur)
        else:
            if abs(cur - cookies[i - 1]) <= abs(cur - cookies[i]):
                res += abs(cur - cookies[i - 1])
                cur = cookies[i - 1]
                cookies.remove(cur)
            else:
                res += abs(cur - cookies[i])
                cur = cookies[i]
                cookies.remove(cur)
print(res)