from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

S = input()


EX_pair_cnt = defaultdict(int)
X_cnt = [0] * 3

def calc_mex(x:int, y:int, z:int):
    for i in range(4):
        if i != x and i != y and i != z:
            return i
    return None

res = 0
for i in range(N - 1, -1, -1):
    match S[i]:
        case "M":
            m_num = A[i]
            for k, v in EX_pair_cnt.items():
                mex = calc_mex(k[0], k[1], m_num)
                assert mex is not None
                res += mex * v
        case "E":
            e_num = A[i]
            for x_num in range(3):
                if e_num < x_num:
                    minor, major = e_num, x_num
                else:
                    minor, major = x_num, e_num
                EX_pair_cnt[(minor, major)] += X_cnt[x_num]
        case "X":
            X_cnt[A[i]] += 1

print(res)