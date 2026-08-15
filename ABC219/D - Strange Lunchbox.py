N = int(input())
X, Y = map(int, input().split())
INF = float("inf")

lunchs = [tuple(map(int, input().split())) for _ in range(N)]
dp = {0: 0}


def tuple2key(a:int, b:int):
    return a * 1000 + b
def key2tuple(k:int):
    return tuple(divmod(k, 1000))

for i in range(N):
    next_dp = {}
    la, lb = lunchs[i]
    for key, val in dp.items():
        a, b = key2tuple(key)
        next_dp[key] = min(next_dp.get(key, INF), val)
        next_key = tuple2key(min(a + la, X), min(b + lb, Y))
        next_dp[next_key] = min(next_dp.get(next_key, INF), val + 1)
    dp = next_dp
    # print(dp)

print(dp.get(tuple2key(X, Y), -1))