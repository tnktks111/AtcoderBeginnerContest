import math
T = int(input())

for _ in range(T):
    C, D = map(int, input().split())
    K = len(str(C + D))
    res = 0
    for k in range(1, K + 1):
        lower_bound = max(10 ** (k - 1) - C, 1)
        upper_bound = min(10 ** k - C - 1, D)
        if lower_bound > upper_bound:
            continue
        
        lower_root = math.isqrt(C * 10 ** k + C + lower_bound - 1)
        upper_root = math.isqrt(C * 10 ** k + C + upper_bound)
        res += (upper_root - lower_root)
    print(res)