INF = float("inf")

# 最小のa ... ma
# 差額が小さいものから見ていく
# ma + b > a ならクーポンを使わないほうが得寄り(p個あるとする)
# pが過半数ならクーポンが余るので、まだクーポンを使ってないものから差額が大きいものを選んでクーポンを適用
# pが過半数ではないなら、クーポンが足りない分maを加算
def solve():
    N = int(input())
    prices = []
    ma = INF
    for _ in range(N):
        a, b = map(int, input().split())
        ma = min(ma, a)
        prices.append((a, b))

    prices.sort(key=lambda x: x[0] - x[1])
    tmp = 0
    for i in range(N):
        if i >= (N + 1) // 2:
            tmp += prices[i][1]
        elif N % 2 == 1 and i == N // 2:
            if prices[i][0] <= prices[i][1] + ma:
                tmp += prices[i][0]
            else:
                tmp += prices[i][1] + ma
        else:
            if prices[i][0] <= prices[i][1] + 2 * ma:
                tmp += prices[i][0]
            else:
                tmp += prices[i][1] + 2 * ma
    return tmp

T = int(input())
for _ in range(T):
    print(solve())