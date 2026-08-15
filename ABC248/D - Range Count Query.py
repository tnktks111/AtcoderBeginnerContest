from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
rec = defaultdict(list) #num:idx(0-indexed)
for i in range(N):
    rec[A[i]].append(i)

def nibutan(tar:int, l:list) -> int:
    if tar < l[0]:
        return 0
    if tar >= l[-1]:
        return len(l)
    left, right = 0, len(l) - 1
    while right - left > 1:
        mid = (left + right) // 2
        if l[mid] <= tar:
            left = mid
        else:
            right = mid
    return left + 1


for _ in range(Q):
    query = list(map(int, input().split()))
    if query[2] in rec:
        print(nibutan(query[1] - 1, rec[query[2]]) - nibutan(query[0] - 2, rec[query[2]]))
    else:
        print(0)