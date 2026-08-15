from itertools import accumulate
N, T = map(int, input().split())
A = [0] + list(map(int, input().split()))
A_cumsum = list(accumulate(A))

def nibutan(t:int):
    l, r = 0, len(A_cumsum) - 1
    while r - l > 1:
        m = (l + r) // 2
        if A_cumsum[m] > t:
            r = m
        else:
            l = m
    return l

cur = nibutan(T % A_cumsum[-1])
print(cur + 1, (T % A_cumsum[-1]) - A_cumsum[cur])