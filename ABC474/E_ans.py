INF = float("inf")

def solve():
    N = int(input())
    prices = []
    ma = INF
    for _ in range(N):
        a, b = map(int, input().split())
        ma = min(a, ma)
        prices.append((a, b))
    res = INF
    for i in range((1 << N)):
        coupon = 0
        tmp = 0
        for j in range(N):
            if (1 << j) & i:
                tmp += prices[j][0]
                coupon += 1
            else:
                tmp += prices[j][1]
                coupon -= 1
        while coupon < 0:
            tmp += ma
            coupon += 1
        res = min(res, tmp)
    return res


T = int(input())
for _ in range(T):
    print(solve())