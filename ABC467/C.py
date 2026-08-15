from copy import deepcopy
N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_adjsum = [(A[i] + A[i + 1]) % M for i in range(N - 1)]
# print(A_adjsum)

res = float("inf")
for first_add in range(M):
    tmpsum = deepcopy(A_adjsum)
    tmpsum[0] = (tmpsum[0] + first_add) % M
    tmp_res = first_add
    # print("first", tmpsum)
    diffs = [0] * N
    diffs[0] = first_add
    for i in range(N - 2):
        diff = (B[i] - tmpsum[i]) % M
        tmp_res += diff
        tmpsum[i] = (tmpsum[i] + diff) % M
        tmpsum[i + 1] = (tmpsum[i + 1] + diff) % M
        diffs[i + 1] = diff
        # print(i, tmpsum)
    tmp_res += (B[-1] - tmpsum[-1]) % M
    diffs[-1] = (B[-1] - tmpsum[-1]) % M
    # print(tmp_res)
    # print(tmpsum)
    print(diffs)
    res = min(res, tmp_res)

print(res)