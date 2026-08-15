N = int(input())
A = list(map(int, input().split()))
A_odd = [a for a in A if a & 1]
A_even = [a for a in A if (a & 1) ^ 1]
A_odd.sort()
A_even.sort()

res = -1
if len(A_even) > 1:
    res = max(res, A_even[-1] + A_even[-2])
if len(A_odd) > 1:
    res = max(res, A_odd[-1] + A_odd[-2])
print(res)