N = int(input())
mod = 998244353
res = 0
def f(x:int) -> int:
    d = len(str(x))
    return (x - 10 ** (d - 1) + 1)
def g(d:int) -> int:
    return ((9 * (10 ** (d - 1)) + 1) * 9 * (10 ** (d - 1)) // 2)
digits = len(str(N))
if digits > 1:
    for digit in range(1, digits):
        res = (res + g(digit)) % mod
res = (res + (1 + f(N)) * (f(N)) // 2) % mod
print(res)
