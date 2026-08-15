N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
A.append(0)

#(l, r]の合計値
def calc_sum(l:int, r:int):
    return r * (r + 1) // 2 - l * (l + 1) // 2

def process(i:int, remain:int):
    sup = (A[i] - A[i + 1]) * (i + 1)
    if sup <= remain:
        return (i + 1) * calc_sum(A[i + 1], A[i]), remain - sup
    else:
        p, q = divmod(remain, i + 1)
        res = (i + 1) * calc_sum(A[i] - p, A[i])
        res += q * (A[i] - p)
        return res, 0

amuse = 0
remain = K
for i in range(N):
    addition, remain = process(i, remain)
    amuse += addition
    if remain == 0:
        break
print(amuse)