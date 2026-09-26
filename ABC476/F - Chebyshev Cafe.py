"""
(1, 1) -> (2, 3) 交通費は2
(x+y, x-y) -> (x, y)
(1, 0) -> (5/2, -1/2) マンハッタン距離2
"""

from itertools import accumulate
from bisect import bisect_right

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

N_acc = list(accumulate(range(N + 1)))

res = 0

i_dash_nums = []
j_dash_nums = []

cnt_i_dash = dict()
cnt_j_dash = dict()

for i in range(N):
    for j in range(N):
        i_dash = i + j
        j_dash = i - j
        i_dash_nums.append(i_dash)
        j_dash_nums.append(j_dash)
        cnt_i_dash[i_dash] = cnt_i_dash.get(i_dash, 0) + A[i] * B[j] % M
        cnt_j_dash[j_dash] = cnt_j_dash.get(j_dash, 0) + A[i] * B[j] % M

i_dash_nums.sort()
j_dash_nums.sort()

i_dash_nums_acc = [0]
cnts_i_dash_acc = [0]
for idx, i_dash in enumerate(i_dash_nums):
    if idx != 0 and i_dash == i_dash_nums[idx - 1]:
        i_dash_nums_acc.append(i_dash_nums_acc[-1])
        cnts_i_dash_acc.append(cnts_i_dash_acc[-1])
    else:
        i_dash_nums_acc.append(i_dash_nums_acc[-1] + i_dash * cnt_i_dash[i_dash])
        cnts_i_dash_acc.append(cnts_i_dash_acc[-1] + cnt_i_dash[i_dash])

j_dash_nums_acc = [0]
cnts_j_dash_acc = [0]
for idx, j_dash in enumerate(j_dash_nums):
    if idx != 0 and j_dash == j_dash_nums[idx - 1]:
        j_dash_nums_acc.append(j_dash_nums_acc[-1])
        cnts_j_dash_acc.append(cnts_j_dash_acc[-1])
    else:
        j_dash_nums_acc.append(j_dash_nums_acc[-1] + j_dash * cnt_j_dash[j_dash])
        cnts_j_dash_acc.append(cnts_j_dash_acc[-1] + cnt_j_dash[j_dash])

res = 0
for i in range(N):
    for j in range(N):
        f_ij = 0
        i_dash = i + j
        j_dash = i - j

        # i方向のマンハッタン距離
        i_larger_idx = bisect_right(i_dash_nums, i_dash)
        # print(i_larger_idx, i_dash_nums_acc, i)
        f_ij += (i_dash_nums_acc[-1] - i_dash_nums_acc[i_larger_idx]) - i_dash * (cnts_i_dash_acc[-1] - cnts_i_dash_acc[i_larger_idx])
        f_ij += i_dash * cnts_i_dash_acc[i_larger_idx] - i_dash_nums_acc[i_larger_idx]

        # j方向のマンハッタン距離
        j_larger_idx = bisect_right(j_dash_nums, j_dash)
        f_ij += (j_dash_nums_acc[-1] - j_dash_nums_acc[j_larger_idx]) - j_dash * (cnts_j_dash_acc[-1] - cnts_j_dash_acc[j_larger_idx])
        f_ij += j_dash * cnts_j_dash_acc[j_larger_idx] - j_dash_nums_acc[j_larger_idx]
        # print(f_ij)
        res ^= (f_ij // 2 + i * N + j)

print(res)