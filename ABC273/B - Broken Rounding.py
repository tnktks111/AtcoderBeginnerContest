X, K = map(int, input().split())
def round_half_up(x:int, digit:int):
    q, mod = divmod(x, 10 ** digit)
    if mod < 10 ** digit // 2:
        return q * 10 ** digit
    else:
        return (q + 1) * 10 ** digit

for i in range(1, K + 1):
    X = round_half_up(X, i)
    # print(X)
print(X)

