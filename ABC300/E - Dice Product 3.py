#dpらしい

#逆元
import math
MOD = 998244353
N = int(input())
def dice_divisor_cnt(n:int) -> tuple[bool, tuple[int, int, int]]:
    res = [0, 0, 0]
    while n % 2 == 0:
        n //= 2
        res[0] += 1
    while n % 3 == 0:
        n //= 3
        res[1] += 1
    while n % 5 == 0:
        n //= 5
        res[2] += 1
    if n > 1:
        return False, (-1, -1, -1)
    else:
        return True, tuple(res)

# 2^m * 3^n = 2^a * 3^b * 4^c * 6^dの組み合わせを返す
# a+2c+d=m, b+d=n, abcdは非負整数であることに注意する.
def possible_2_3_4_6_pair(m:int, n:int):
    res = []
    for b in range(n + 1):
        d = n - b
        if d > m:
            continue
        for a in range(m - d + 1):
            double_c  = m - a - d
            if double_c % 2 == 1:
                continue
            res.append((a, b, double_c // 2, d))
    return res

def narabikae_cnt(a:int, b:int, c:int, d:int, e:int, f:int, total:int):
    return math.factorial(total - a) // (math.factorial(b) * math.factorial(c) * math.factorial(d) * math.factorial(e) * math.factorial(f)) * 5 ** a


possible, (m, n, l) = dice_divisor_cnt(N)
if not possible:
    print(0)
    exit()
pairs = possible_2_3_4_6_pair(m, n)
# print(pairs)
res = 0
total = m + n + l
for pair in pairs:
    tmp = narabikae_cnt(total - pair[0] - pair[1] - pair[2] - pair[3] - l, pair[0], pair[1], pair[2], l, pair[3], total)
    res += tmp
print(res, total)
print(res * pow(5 ** total, -1, MOD) % MOD)