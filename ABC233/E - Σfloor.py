X = list(map(int, list(input())))
k = len(X)
res = [0] * (k + 1)
acc = sum(X)
carry = 0

for i in range(k + 1):
    carry, q = divmod(acc + carry, 10)
    res[k - i] = q
    if i != k:
        acc -= X[k - 1 - i]

ans = "".join(map(str, res)).lstrip("0")
print(ans if ans else "0")